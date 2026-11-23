#!/usr/bin/env python3
"""Lookup tool for the BORI Critical Edition e-text (typed by BORI, collated by John D. Smith; UR encoding).
Data: /opt/bori_ce (environment setup script) or set CE=/path. Text (c) BORI, Pune - not stored in this repo.
usage:
  mbh.py v 1.94.88[-93]        verses (constituted text)
  mbh.py ch 1.94               whole chapter
  mbh.py g REGEX [book,...]    grep constituted text (normalized)
  mbh.py star 2 544            star passage 544* of book 2 with apparatus
  mbh.py app 1 1               Appendix I passage 1 of book 1 (with apparatus)
  mbh.py gs REGEX [book,...]   grep supplementary (star+appendix) text
  mbh.py nch 1                 number of chapters / verses in a book
"""
import sys, re, os
D = sys.argv[1] if False else None
BASE = os.environ.get('CE', '/opt/bori_ce')  # filled by the environment setup script

def norm(s):
    return (s.replace('ṃ','ṁ').replace('ṛ','r̥').replace('ṝ','r̥̄').replace('ḷ','l̥').replace("'", '’'))

def load(book):
    with open(os.path.join(BASE, f'MBh{int(book):02d}_UR.txt'), encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l and l[0].isdigit()]

def loadsupp(book):
    with open(os.path.join(BASE, f'Supp{int(book):02d}_UR.txt'), encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f]

def cmd_v(ref):
    b, c, vs = ref.split('.')
    if '-' in vs: v1, v2 = map(int, vs.split('-'))
    else: v1 = v2 = int(vs)
    pre = f'{int(b):02d}{int(c):03d}'
    for l in load(b):
        if l.startswith(pre):
            v = int(l[5:8])
            if v1 <= v <= v2: print(l)

def cmd_ch(ref):
    b, c = ref.split('.')
    pre = f'{int(b):02d}{int(c):03d}'
    for l in load(b):
        if l.startswith(pre): print(l)

def books(arg):
    if arg is None: return range(1, 19)
    return [int(x) for x in arg.split(',')]

def cmd_g(pat, barg=None):
    rx = re.compile(norm(pat))
    for b in books(barg):
        for l in load(b):
            if rx.search(l): print(l)

def cmd_gs(pat, barg=None):
    rx = re.compile(norm(pat))
    for b in books(barg):
        for l in loadsupp(b):
            if rx.search(l): print(f'[S{b:02d}] {l}')

def show_block(book, key):
    lines = loadsupp(book)
    out = []; start=None
    for i,l in enumerate(lines):
        if l.startswith(key):
            if start is None:
                # include preceding apparatus comment lines
                j=i-1; com=[]
                while j>=0 and lines[j].startswith('%'):
                    com.insert(0, lines[j]); j-=1
                out.extend(com); start=i
            out.append(l)
        elif start is not None and not l.startswith('%') and l.strip():
            break
    print('\n'.join(out))

def cmd_star(book, n):
    show_block(book, f'{int(book):02d}*{int(n):04d}')

def cmd_app(book, n):
    show_block(book, f'{int(book):02d}_{int(n):03d}_')

def cmd_nch(book):
    ch = {}
    for l in load(book):
        c = int(l[2:5]); v = int(l[5:8]); ch[c] = max(ch.get(c,0), v)
    print('chapters', len(ch), 'verses(sum of max verse no.)', sum(ch.values()))

if __name__ == '__main__':
    a = sys.argv[1:]
    {'v': lambda: cmd_v(a[1]), 'ch': lambda: cmd_ch(a[1]),
     'g': lambda: cmd_g(a[1], a[2] if len(a)>2 else None),
     'gs': lambda: cmd_gs(a[1], a[2] if len(a)>2 else None),
     'star': lambda: cmd_star(a[1], a[2]), 'app': lambda: cmd_app(a[1], a[2]),
     'nch': lambda: cmd_nch(a[1])}[a[0]]()
