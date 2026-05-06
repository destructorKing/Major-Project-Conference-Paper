import re
from pathlib import Path
text = Path('Draft.tex').read_text(encoding='utf-8')
cites = re.findall(r'\\cite\{([^}]+)\}', text)
keys = set()
for c in cites:
    for k in c.split(','):
        keys.add(k.strip())
bibkeys = set(re.findall(r'\\bibitem\{([^}]+)\}', text))
print('Citations:', len(keys))
print('Bibitems:', len(bibkeys))
print('Missing:', sorted(keys - bibkeys))
print('Unused:', sorted(bibkeys - keys)[:20])
