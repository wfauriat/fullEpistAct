import re,sys
pages=open(sys.argv[1],encoding='utf8').read().split('\f')
pats=[l.strip() for l in open(sys.argv[2],encoding='utf8') if l.strip()]
for p in pats:
  rx=re.compile(p,re.I)
  hits=[(i+1,m) for i,pg in enumerate(pages) for m in rx.finditer(pg)]
  pgs=sorted(set(h[0] for h in hits))
  out=f'## {p} : {len(hits)} hits, pages {pgs[:14]}{"..." if len(pgs)>14 else ""}'
  print(out)
  shown=0
  for i,m in hits:
    if shown>=int(sys.argv[3]) : break
    pg=pages[i-1];s=max(0,m.start()-110);e=min(len(pg),m.end()+110)
    print(f'   p{i}: …'+re.sub(r'\s+',' ',pg[s:e])+'…');shown+=1
