from yaml import safe_load
from pathlib import Path

#TODO: Make this a user input
BOOK_PATH = Path('./book')

def make_redirect_html(url):
    #From https://theorangeone.net/posts/redirecting-static-pages/
    return f'''
<!DOCTYPE html>
<html>
  <head>
    <title>Redirecting...</title>
    <link rel="canonical" href="{url}" />
    <meta charset="utf-8" />
    <meta http-equiv="refresh" content="0; url={url}" />
  </head>
  <body>
    <p>Redirecting...</p>
  </body>
</html>
'''

if __name__ == '__main__':
    with open(BOOK_PATH / '_redirect.yml', 'rt') as f:
        redirect_urls = safe_load(f.read())
    
    for url in redirect_urls:
        html_str = make_redirect_html(url['url_to'])
        
        from_path = BOOK_PATH / '_build' / 'html' / url['url_from']
        from_path = from_path.with_suffix('.html')

        to_path = from_path.parent / url['url_to']
        to_path.resolve()

        if not to_path.is_file():
            print('Warning: no file found at', to_path, 'from relative path', url['url_to'])

        from_path.parent.mkdir(parents=True, exist_ok=True)
        from_path.write_text(html_str)
        # with open(from_path, 'wt') as f:
        #     f.write(html_str)
    pass