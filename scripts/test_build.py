"""
TODO:
> Make separate test content that is kept seperately from the book content
"""

from build_pdf import _book_to_pdf
import asyncio

BUILD_PATH = './book/_build/html/'

pdf_file = './scripts/test_pdf.pdf'

content_files = [
    {
        'file' : BUILD_PATH + 'content/intro/intro.html'
    },
    {
        'part' : 'The Python Standard Library',
        'chapters' : [
            {
                'file' : BUILD_PATH + 'content/standard-library/basics/intro.html',
                'sections' : [
                    {'file' : BUILD_PATH + 'content/standard-library/basics/variables.html'},
                    {'file' : BUILD_PATH + 'content/standard-library/basics/comments.html'},
                    {'file' : BUILD_PATH + 'content/standard-library/basics/types.html'}
                ]
            },
            {
                'file' : BUILD_PATH + 'content/standard-library/data-structures/intro.html',
                'sections' : [
                    {'file' : BUILD_PATH + 'content/standard-library/data-structures/tuple.html'},
                    {'file' : BUILD_PATH + 'content/standard-library/data-structures/lists.html'},
                    {'file' : BUILD_PATH + 'content/standard-library/data-structures/dictionaries.html'}
                ]
            }
        ]
    },
    {
        'part' : 'Scientific Packages',
        'chapters' : [
            {
                'file' : BUILD_PATH + 'content/scientific-packages/numpy/intro.html',
                'sections' : [
                    {'file' : BUILD_PATH + 'content/scientific-packages/numpy/arrays.html'},
                    {'file' : BUILD_PATH + 'content/scientific-packages/numpy/array-methods.html'},
                    {'file' : BUILD_PATH + 'content/scientific-packages/numpy/where.html'}
                ]
            },
            {
                'file' : BUILD_PATH + 'content/scientific-packages/matplotlib/intro.html',
                'sections' : [
                    {'file' : BUILD_PATH + 'content/scientific-packages/matplotlib/simple.html'},
                    {'file' : BUILD_PATH + 'content/scientific-packages/matplotlib/subplots.html'}
                ]
            }
        ]
    }
]


asyncio.get_event_loop().run_until_complete(_book_to_pdf(content_files, pdf_file))