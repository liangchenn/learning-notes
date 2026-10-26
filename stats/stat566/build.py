#!/usr/bin/env python3
"""Rebuild the four notes and combined volume using LuaLaTeX."""
import pathlib
import shutil
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ['stat566-note01', 'stat566-note02', 'stat566-note3', 'stat566-note5', 'stat566-all']

def main():
    engine = shutil.which('lualatex')
    if not engine:
        raise SystemExit('LuaLaTeX is required (TeX Live / MacTeX).')
    out = ROOT / 'build'
    out.mkdir(exist_ok=True)
    for doc in DOCS:
        for pass_number in range(4):
            result = subprocess.run([engine, '-interaction=nonstopmode', '-halt-on-error',
                '-file-line-error', '-output-directory=build', doc + '.tex'],
                cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode:
                print(result.stdout[-12000:])
                raise SystemExit(f'Compilation failed: {doc}')
            pass_log = (out / (doc + '.log')).read_text(errors='replace')
            if pass_number >= 1 and not any(message in pass_log for message in
                ['Rerun to get cross-references right', 'Rerun to get outlines right']):
                break
        log = (out / (doc + '.log')).read_text(errors='replace')
        problems = [line for line in log.splitlines() if any(s in line for s in
            ['Overfull', 'Missing character:', 'undefined references', 'undefined citations'])]
        if problems:
            raise SystemExit(f'{doc}: ' + '\n'.join(problems))
        shutil.copy2(out / (doc + '.pdf'), ROOT / (doc + '.pdf'))
        print(f'Built {doc}.pdf')

if __name__ == '__main__':
    main()
