import sqlite3,sys
def varint(b,i):
  r=s=0
  while True:
    c=b[i];i+=1;r|=(c&0x7f)<<s;s+=7
    if c<0x80:return r,i
def parse(b):
  i=0;out=[]
  try:
    while i<len(b):
      k,i=varint(b,i);f,w=k>>3,k&7
      if f==0:return None
      if w==0:v,i=varint(b,i);out.append((f,'v',v))
      elif w==1:out.append((f,'64',b[i:i+8]));i+=8
      elif w==5:out.append((f,'32',b[i:i+4]));i+=4
      elif w==2:
        l,i=varint(b,i);sub=b[i:i+l];i+=l
        if i>len(b):return None
        p=parse(sub) if l>0 else []
        try:t=sub.decode('utf8');pr=all(31<ord(c)<0x10000 or c in'\n\t' for c in t)
        except:pr=False
        out.append((f,'s',t[:60]) if pr and (p is None or len(t)<40 or not p) else (f,'m',p) if p else (f,'b',l))
      else:return None
    return out
  except Exception:return None
def show(t,d=0):
  for f,ty,v in t:
    if ty=='m':print('  '*d+f'{f}:');show(v,d+1)
    else:print('  '*d+f'{f} {ty} {v}')
if __name__=='__main__':
 db=sqlite3.connect(sys.argv[1])
 row=db.execute('select data from gen_metadata where idx=?',(int(sys.argv[2]),)).fetchone()
 show(parse(row[0]))
