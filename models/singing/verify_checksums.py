"""Verify all files listed in a local SHA256SUMS manifest. Python standard library only."""
import argparse,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('folder',nargs='?',default='.');a=p.parse_args()
root=Path(a.folder).resolve();count=0
for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
    expected,name=line.split('  ',1);target=(root/name).resolve()
    assert target.is_relative_to(root), 'Manifest path escapes root'
    h=hashlib.sha256()
    with target.open('rb') as f:
        for b in iter(lambda:f.read(8388608),b''):h.update(b)
    assert h.hexdigest()==expected, 'Hash mismatch: '+name
    count+=1
print('Verified',count,'files')
