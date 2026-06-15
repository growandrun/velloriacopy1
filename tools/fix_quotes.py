import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\velloriacopy1\tools\index.template.html'
text = open(path, encoding='utf-8').read()

before = text
# Replace curly/smart double quotes with straight ASCII double quotes
text = text.replace('“', '"').replace('”', '"')
# Also replace curly single quotes just in case
text = text.replace('‘', "'").replace('’', "'")

count = sum(1 for a, b in zip(before, text) if a != b)
print(f'Replaced {count} curly-quote characters')

open(path, 'w', encoding='utf-8').write(text)
print('Done.')
