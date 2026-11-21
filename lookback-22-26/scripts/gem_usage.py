import sqlite3,sys,glob,os,json
sys.path.insert(0,os.path.dirname(__file__))
from pb import parse
def get(t,f):
  return [v for ff,ty,v in (t or []) if ff==f]
def usage(blob):
  t=parse(blob)
  m8=[x for x in get(t,1) if isinstance(x,list)]
  if not m8 or not isinstance(m8[0],list):return None
  u=get(m8[0],4); ctx=get(m8[0],9)
  if not u or not isinstance(u[0],list):return None
  d={f:v for f,ty,v in u[0] if ty=='v'}
  model=[v for f,ty,v in t if f==19]
  c=None
  if ctx and isinstance(ctx[0],list):
    c10=get(ctx[0],10)
    if c10 and isinstance(c10[0],list): c=dict((f,v) for f,ty,v in c10[0] if ty=='v').get(1)
  return d,(model[0] if model else None),c
if __name__=='__main__':
  db=sqlite3.connect(sys.argv[1])
  for idx,blob in db.execute('select idx,data from gen_metadata order by idx'):
    print(idx,usage(blob))
