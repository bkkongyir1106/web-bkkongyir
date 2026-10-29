#!/usr/bin/env python3
"""Check a fresh Hugo output for broken local links and content regressions.

Usage: python3 scripts/check_site.py public
Uses only the Python standard library; it does not contact external services.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

root = Path(sys.argv[1] if len(sys.argv) > 1 else 'public').resolve()
class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(text)
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

documents = {p: Document(p.read_text()) for p in root.rglob('*.html')}
errors = []
checked = 0
for path, doc in documents.items():
    base = '/' + path.relative_to(root).as_posix()
    for link in doc.links:
        url = urlsplit(link)
        if url.scheme not in ('', 'http', 'https') or (url.netloc and url.netloc not in ('bkkongyir.netlify.app', 'localhost:1313')):
            continue
        resolved = urlsplit(urljoin(base, link))
        target = root / unquote(resolved.path).lstrip('/')
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'{path.relative_to(root)}: missing {link}')
            continue
        checked += 1
        # Wowchemy's publication archive uses #2 as a JS filter, not an ID.
        if target == root / 'publication/index.html' and re.fullmatch(r'[0-9]+', resolved.fragment) and f'pubtype-{resolved.fragment}' in target.read_text():
            continue
        if resolved.fragment and target in documents and unquote(resolved.fragment) not in documents[target].ids:
            errors.append(f'{path.relative_to(root)}: missing anchor {link}')

home = root / 'index.html'
text = home.read_text()
for section in ('about', 'research', 'reports', 'teaching', 'projects', 'cv', 'contact'):
    if section not in documents[home].ids:
        errors.append(f'Missing homepage section: {section}')
for value in ('Gustavus Adolphus College', 'July 2026', 'Bootstrap Regression', 'A Model for Pricing Insurance'):
    if value not in text:
        errors.append(f'Missing expected content: {value}')
for value in ('bagyare@', 'bosafoagyare/', 'Benjamin Osafo', 'Benjamin Asafo', 'DistGD', 'UA-200851324-1', 'G-GPL6087QSL'):
    for path in documents:
        if value.lower() in path.read_text().lower():
            errors.append(f'Inherited identity/tracking in {path.relative_to(root)}: {value}')
for old in ('osafoagyare-bayes-2020', 'osafoagyare-expectile-factorization-2024'):
    alias = root / 'publication' / old / 'index.html'
    if not alias.exists() or 'http-equiv=refresh' not in alias.read_text().replace('"', ''):
        errors.append(f'Missing compatibility redirect: {old}')
if errors:
    print('\n'.join(sorted(set(errors))))
    sys.exit(1)
print(f'PASS: {len(documents)} HTML files; {checked} local links/assets; required sections, profile updates, and legacy page redirects.')
print('External links, Netlify form delivery, and deployed attachment redirects require separate checks.')
