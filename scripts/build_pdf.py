"""
This is a work in progress, it will be converted to work using commandline
commands.

Used to create a pdf book with 
> contents potentially re-arranged
> page breaks between pages
> optional page dividers
> contents metadata

Much of this script is adapted from:
https://github.com/executablebooks/jupyter-book/blob/v0.8.3/jupyter_book/pdf.py
with only the pyppeteer method being used.

TODO:
> Make sure there aren't memory leaks
> Show a progressbar
> Give each page a header with 'Part \t Chapter \t Section'

> Alt toc not implemented. Need to think of how I want to format it
> Section numbering not implemented
> Find the font used by the book for the title pages and the header


> Print progress in the terminal as it builds
> Test if the PdfFileMerger might be better for the job than the writer (maintaning internal links, ect)
> There are opportunities to render browser pages concurrently, come back to this
"""

from ctypes import alignment
from pathlib import Path
import asyncio
import os
import re
from io import BytesIO, StringIO

from yaml import safe_load

from pyppeteer import launch
from PyPDF2 import PdfFileReader, PdfFileWriter
from fpdf import FPDF

#TODO: Replace PyPDF2 with pdrw
from pdfrw import PdfReader, PdfWriter
from pagelabels import PageLabels, PageLabelScheme


FONT = 'helvetica'
CELL_HEIGHT_FACTOR = 0.8
PAGE_NUMBER_FONT_SIZE = 10
PART_TITLE_FONT_SIZE = 24

TOC_PAGE_HEIGHT = 290
TOC_PAGE_WIDTH = 200
TOC_NUMBER_WIDTH = 20
TOC_TITLE_FONT_SIZE = 16
TOC_INDENT_SIZE = 4
TOC_FONT_SIZES = {
    'part' : 12, 
    'chapter' : 10, 
    'section' : 8
    }
TOC_UNDERLINE_WIDTH = 1


def book_to_pdf(book_path, pdf_file, cover_path = None, alt_toc_file = None):
    """
    Convert book to pdf.

    Parameters
    ----------
    book_path : str
    pdf_file : str
    alt_toc_file : str
        A path to an alternate toc, which may re-arrange contents
        or insert additional html or pdf pages.
    """

    # Make content_files using book toc and alt_toc
    content_files = _contents_from_toc(book_path, alt_toc_file)

    cover = None
    cover_file = None
    if cover_path:
        #with open(cover_path, 'rb') as f:
        cover_file = open(cover_path, 'rb')
    cover = PdfFileReader(cover_file)

    asyncio.get_event_loop().run_until_complete(_book_to_pdf(content_files, pdf_file, cover))
    cover_file.close()


def _contents_from_toc(book_path, alt_toc_file):
    #TODO: check that toc file exists
        
    with open(os.path.join(book_path, '_toc.yml'), 'r') as f:
        toc = safe_load(f)
    
    _prepend_path_to_toc(os.path.join(book_path, '_build', 'html'), toc, '.html')

    if not alt_toc_file:
        #TODO: check that the toc is an array
        return toc


def _prepend_path_to_toc(path, toc, extension = ''):
    #TODO: check if files exist

    if 'file' in toc.keys():
        toc['file'] = os.path.join(path, toc['file'] + extension)

    parts = toc.get("parts")

    if parts:
        for part in parts:
            _prepend_path_to_toc(path, part, extension)
        return

    chapters = toc.get("chapters")

    if chapters:
        for chapter in chapters:
            _prepend_path_to_toc(path, chapter, extension)
        return

    sections = toc.get("sections")

    if sections:
        for section in sections:
            _prepend_path_to_toc(path, section, extension)


async def _book_to_pdf(content, pdf_file, cover = None):
    pdf_writer = PdfFileWriter()
    
    if cover:
        pdf_writer.appendPagesFromReader(cover)
        pdf_writer.addBookmark('Cover', 0)

    browser = await launch(args = ['--no-sandbox'])
    browser_page = await browser.newPage()
    
    
    await _content_to_pdf_pages(content, browser_page)
    
    toc_page_num = pdf_writer.getNumPages()
    pdf_writer.appendPagesFromReader(PdfFileReader(_toc_pdf_pages_from_content(content)))
    pdf_writer.addBookmark('Contents', toc_page_num)

    content_page_num = pdf_writer.getNumPages()
    _compile_pdf_content(pdf_writer, content)
    
    with open(pdf_file, 'wb') as f:
        pdf_writer.write(f)

    reader = PdfReader(pdf_file)
    #pdf_stream.close()
    labels = PageLabels.from_pdf(reader)

    #TODO: suppress numbering
    if cover:
        labels.append(
            PageLabelScheme(
                startpage = 0,
                prefix = 'Cover'
            )
        )

    # TOC and preceding cover pages
    labels.append(
        PageLabelScheme(
            startpage = 1,
            style = 'roman lowercase',
            firstpagenum = 1
        )
    )

    #Main contents
    labels.append(
        PageLabelScheme(
            startpage = content_page_num,
            style = 'arabic',
            firstpagenum = 1
        )
    )

    labels.write(reader)
    writer = PdfWriter()
    writer.trailer = reader
    writer.write(pdf_file)


async def _content_to_pdf_pages(content, browser_page, numbered = False, page_number = 1):
    file_path = content.get('file')
    file_type = content.get('type', 'html')
    caption = content.get('caption')
    content_numbered = content.get('numbered', numbered)

    #content_page_num = page_number
    if file_path and file_type == 'html':
        pdf = PdfFileReader(await _html_to_pdf(file_path, browser_page))
        
        pdf = _pdf_number_overlay(await _html_to_pdf(file_path, browser_page), page_number)
        content['pdf'] = pdf
        content['page_number'] = page_number

        page_number += pdf.getNumPages()

        if not caption:
            content['caption'] = _infer_title(await browser_page.content())
        print('PDF of page complete: ', content['caption'])
            

    parts = content.get('parts')
    if parts:
        for part in parts:
            if not part.get('file'):
                caption = part.get('caption', '')
                
                #print("Part ", caption)

                pdf = _make_part_title_page(caption, page_number)
                part['pdf'] = pdf
                part['page_number'] = page_number

                #print(" Page Num: ", page_number)
                #print('Num Pages: ', pdf.getNumPages())
                page_number += pdf.getNumPages()
                
            page_number = await _content_to_pdf_pages(part, browser_page, numbered = content_numbered, page_number = page_number)
            #print('Num Pages end: ', page_number)
        return page_number


    sections = content.get('chapters')
    if not sections:
        sections = content.get('sections')
    
    if sections:
        for section in sections:
            page_number = await _content_to_pdf_pages(section, browser_page, numbered = content_numbered, page_number = page_number)
        return page_number
    
    return page_number


def _toc_pdf_pages_from_content(content):
    page = FPDF()
                
    page.add_page()
    page.set_font(FONT, size = TOC_TITLE_FONT_SIZE)
    
    page.cell(0, TOC_TITLE_FONT_SIZE * 1.3, 'Table of Contents', border = 'B', ln = 1)

    _toc_content(page, content)

    return BytesIO(page.output(dest = 'S'))


def _toc_content(page, content, section_type = '', level = -1):
    if 'page_number' in content.keys():
        print('Making TOC entry for ', content.get('caption', ''))
        font_size = TOC_FONT_SIZES[section_type]
        page.set_font(FONT, size = font_size)
        
        indent_size = TOC_INDENT_SIZE * level
        page.set_x(page.get_x() + indent_size)
        height = CELL_HEIGHT_FACTOR * font_size
        page.cell(TOC_PAGE_WIDTH - indent_size - TOC_NUMBER_WIDTH, height, txt = content.get('caption', ''), border = 'B')
        page.cell(0, height, txt = str(content['page_number']), align = 'R', ln = 1)


    sections = content.get('parts')
    section_type = 'part'
    
    if not sections:
        sections = content.get('chapters')
        section_type = 'chapter'
    
    if not sections:
        sections = content.get('sections')
        section_type = 'section'
    
    if sections:
        for section in sections:
            _toc_content(page, section, section_type, level + 1)


def _compile_pdf_content(pdf_writer, content, parent_bookmark = None):
    caption = content.get('caption', '')
    pdf = content.get('pdf')

    content_bookmark = None
    if pdf:
        page_num = pdf_writer.getNumPages()
        pdf_writer.appendPagesFromReader(pdf)
        content_bookmark = pdf_writer.addBookmark(caption, page_num, parent_bookmark)

    sections = content.get('parts')
    if not sections:
        sections = content.get('chapters')
    if not sections:
        sections = content.get('sections')
    if sections:
        for section in sections:
            _compile_pdf_content(pdf_writer, section, content_bookmark)


async def _html_to_pdf(html_file, page): #pdf_writer):
    # Should I be making a new page each time instead?
    # If I need to edit html content then use page.setContent() instead of goto

    # Absolute path is needed
    html_file = Path(html_file).resolve()

    #This doesn't work. Need to figure out a way to alter page contents
    # with open(html_file, 'rt') as f:
    #     html = f.read()
    # await page.setContent(html)
    # await page.reload({"waitUntil": ["networkidle0"]})

    # Waiting for networkidle0 seems to let mathjax render
    await page.goto(f"file:///{html_file}", {"waitUntil": ["networkidle0"]})
    # Give it *some* margins to make it look a little prettier
    # I just made these up
    page_margins = {"left": "0in", "right": "0in", "top": ".5in", "bottom": ".5in"}
    await page.addStyleTag(
        {
            "content": """
                div.cell_input {
                    -webkit-column-break-inside: avoid;
                    page-break-inside: avoid;
                    break-inside: avoid;
                }
                div.cell_output {
                    -webkit-column-break-inside: avoid;
                    page-break-inside: avoid;
                    break-inside: avoid;
                }
         """
        }
    )
    return BytesIO(await page.pdf({"margin": page_margins}))
    #pdf_writer.appendPagesFromReader(PdfFileReader(BytesIO(await page.pdf({"margin": page_margins}))))


def _make_part_title_page(caption, page_number):
    page = FPDF()
                
    page.add_page()
    page.set_font(FONT, size = PAGE_NUMBER_FONT_SIZE)
    page.cell(0, PAGE_NUMBER_FONT_SIZE * 1.3, txt = str(page_number), align = 'R', ln = 2)
    page.set_font(FONT, size = PART_TITLE_FONT_SIZE)
    page.cell(0, PART_TITLE_FONT_SIZE * 1.3, 'Part', border = 'B', ln = 2)
    page.cell(0, 30, caption)

    return PdfFileReader(BytesIO(page.output(dest = 'S')))


def _pdf_number_overlay(pdf_stream, page_number):
    pdf_reader = PdfFileReader(pdf_stream)
    pdf_writer = PdfFileWriter()

    for i in range(pdf_reader.getNumPages()):
        num_page = FPDF()

        num_page.add_page()
        #num_page.line(0, 0.1, TOC_PAGE_WIDTH, 0.2)
        num_page.set_font(FONT, size = PAGE_NUMBER_FONT_SIZE)
        num_page.cell(0, PAGE_NUMBER_FONT_SIZE * CELL_HEIGHT_FACTOR, txt = str(page_number), align = 'R')

        num_page = PdfFileReader( BytesIO(num_page.output(dest = 'S')) ).getPage(0)

        page = pdf_reader.getPage(i)
        #page.mergePage(num_page)
        num_page.mergePage(page)

        pdf_writer.insertPage(num_page, i)

        page_number += 1

    #return pdf_reader

    pdf_stream = BytesIO()
    pdf_writer.write(pdf_stream)
    return PdfFileReader(pdf_stream)
    
    

def _infer_title(html):
    RE_PATTERN = r'\<h1\>(.*)\<\/h1\>'

    match = re.search(RE_PATTERN, html, re.MULTILINE + re.DOTALL)

    if match:
        #Solution borrowed from
        #https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
        clean = re.compile('<.*?>')
        title =  re.sub(clean, '', match.group(0))

        title = re.sub('¶', '', title) #Pilcrow sign, using the unicode code doesn't seem to work
        title = re.sub(u'(\u2018|\u2019)', "'", title) #Left and right quote characters

        return title
        #I'm not sure about using this character directly in the code...
        #return re.sub('¶', '', title)
    
    return None