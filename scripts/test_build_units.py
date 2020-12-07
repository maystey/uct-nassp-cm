from build_pdf import _infer_title

html_file = 'book/_build/html/content/intro.html'

with open(html_file, 'r') as f:
    html = f.read()

print(_infer_title(html))