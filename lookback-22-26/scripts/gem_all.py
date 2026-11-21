import sqlite3,sys,os,collections,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pb import parse
def get(t,f): return [v for ff,ty,v in (t or []) if ff==f]
base='/home/ai-user/.gemini/antigravity-cli/'
S=sqlite3.connect(base+'conversation_summaries.db')
convs=S.execute("select conversation_id,agent_name,parent_conversation_id,title,last_modified_time,step_count from conversation_summaries where workspace_uris like '%review_epist%' order by last_modified_time").fetchall()
res=[];G=collections.Counter();GM=collections.Counter()
for cid,ag,par,title,lm,steps in convs:
  p=base+'conversations/'+cid+'.db'
  if not os.path.exists(p): continue
  db=sqlite3.connect(p);tok=collections.Counter();models=collections.Counter();n=0;maxctx=0
  for (blob,) in db.execute('select data from gen_metadata'):
    t=parse(blob)
    m=[x for x in get(t,1) if isinstance(x,list)]
    if not m: continue
    u=[x for x in get(m[0],4) if isinstance(x,list)]
    if not u: continue
    d={f:v for f,ty,v in u[0] if ty=='v'};n+=1
    tok['new_in']+=d.get(2,0);tok['cached_in']+=d.get(5,0);tok['out']+=d.get(3,0);tok['f9']+=d.get(9,0);tok['f10']+=d.get(10,0)
    maxctx=max(maxctx,d.get(2,0)+d.get(5,0))
    mo=[v for f,ty,v in m[0] if f==21] or [v for f,ty,v in m[0] if f==19]
    models[mo[0] if mo else '?']+=1
  for k,v in tok.items():G[k]+=v
  G['calls']+=n
  for k,v in models.items():GM[k]+=v
  res.append(dict(cid=cid[:8],agent=ag,parent=par[:8],title=title,lm=lm,steps=steps,calls=n,maxctx=maxctx,models=dict(models),**tok))
json.dump(res,open(sys.argv[1],'w'),indent=0)
print(G);print(GM)
for r in res: print(r['lm'][5:16],r['cid'],r['agent'] or '-',r['parent'] or '-',r['calls'],'in',(r.get('new_in',0)+r.get('cached_in',0))//1000,'k out',r.get('out',0)//1000,'k maxctx',r['maxctx']//1000,list(r['models']),r['title'][:40])
