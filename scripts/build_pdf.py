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
> Make in in-text table of contents
> Give each page a header with 'Part \t Chapter \t Section'
> Insert page numbers

> Alt toc not implemented. Need to think of how I want to format it
> Section numbering not implemented
> Find the font used by the book for the title pages and the header


> Print progress in the terminal as it builds
> Test if the PdfFileMerger might be better for the job than the writer (maintaning internal links, ect)
> There are opportunities to render browser pages concurrently, come back to this
"""

from pathlib import Path
import asyncio
import os
import re
from io import BytesIO

from yaml import safe_load

from pyppeteer import launch
from PyPDF2 import PdfFileReader, PdfFileWriter
from fpdf import FPDF


def book_to_pdf(book_path, pdf_file, alt_toc_file = None):
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

    asyncio.get_event_loop().run_until_complete(_book_to_pdf(content_files, pdf_file))


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

    for content in toc:
        if 'file' in content.keys():
            content['file'] = os.path.join(path, content['file'] + extension)

        
        sections = content.get('chapters')

        if not sections:
            sections = content.get('sections')
        
        if sections:
            _prepend_path_to_toc(path, sections, extension)


async def _book_to_pdf(content_files, pdf_file):
    
    #check first file to see if numbered

    pdf_writer = PdfFileWriter()
    
    browser = await launch(args = ['--no-sandbox'])
    browser_page = await browser.newPage()
    
    await _content_to_pdf(content_files, browser_page, pdf_writer)

    with open(pdf_file, 'wb') as f:
        pdf_writer.write(f)


async def _content_to_pdf(content_files, browser_page, pdf_writer, numbered = False, parent_bookmark = None, level = 0):
    for content in content_files:
        file_path = content.get('file')
        file_type = content.get('type', 'html')
        part = content.get('part')
        title = content.get('title')
        content_numbered = content.get('numbered', numbered)

        page_num = pdf_writer.getNumPages()

        if file_path and file_type == 'html':
            await _html_to_pdf(file_path, browser_page, pdf_writer)

            if not title:
                title = _infer_title(await browser_page.content())
        else:
            #print('The file ', file_path, ' was not used. Only html and pdf files are supported.')        
            file_path = None
            
        content_bookmark = None
        if part:
            if not file_path:
                page = FPDF()
                
                page.add_page()
                #page.set_margins(20, 40)
                page.set_font('Arial', size = 24)
                
                page.cell(0, 30, 'Part', border = 'B', ln = 2)
                page.cell(0, 30, part)

                #with BytesIO(page.output(dest = 'S')) as page_stream:
                page_stream = BytesIO(page.output(dest = 'S'))
                #print(page_stream)
                pdf_writer.addPage(PdfFileReader(page_stream).getPage(0))
                #pdf_writer.addBlankPage()

            content_bookmark = pdf_writer.addBookmark(part, page_num, parent_bookmark)
        elif title:
            content_bookmark = pdf_writer.addBookmark(title, page_num, parent_bookmark)

        sections = content.get('chapters')
        
        if not sections:
            sections = content.get('sections')

        if sections:
            await _content_to_pdf(sections, browser_page, pdf_writer, 
                numbered = content_numbered, 
                parent_bookmark = content_bookmark,
                level = level + 1)


async def _html_to_pdf(html_file, page, pdf_writer):
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
    pdf_writer.appendPagesFromReader(PdfFileReader(BytesIO(await page.pdf({"margin": page_margins}))))


def _infer_title(html):
    RE_PATTERN = r'\<h1\>(.*)\<\/h1\>'

    match = re.search(RE_PATTERN, html, re.MULTILINE + re.DOTALL)

    if match:
        #Solution borrowed from
        #https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
        clean = re.compile('<.*?>')
        title =  re.sub(clean, '', match.group(0))

        #I'm not sure about using this character directly in the code...
        return re.sub('¶', '', title)
    
    return None