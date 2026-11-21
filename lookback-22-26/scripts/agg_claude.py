import json,glob,os,sys,collections
roots=['/home/ai-user/.claude/projects/-home-ai-user-Documents-Sandbox-review-epist-ag','/home/ai-user/.claude/projects/-home-ai-user-Documents-Sandbox-review-epist-ag-monographie']
rows=[]
for r in roots:
  for f in sorted(glob.glob(r+'/*.jsonl')+glob.glob(r+'/*/subagents/*.jsonl')):
    seen={};ts=[];models=collections.Counter();nuser=0;first=None;entry=set();agent=None;slug=None
    for line in open(f,errors='ignore'):
      try:d=json.loads(line)
      except:continue
      t=d.get('timestamp')
      if t:ts.append(t)
      if d.get('entrypoint'):entry.add(d['entrypoint'])
      if d.get('agentId'):agent=d['agentId']
      if d.get('slug'):slug=d['slug']
      if d.get('type')=='user' and not d.get('isMeta'):
        m=d.get('message',{});c=m.get('content')
        txt=c if isinstance(c,str) else ' '.join(x.get('text','') for x in c if isinstance(x,dict) and x.get('type')=='text') if isinstance(c,list) else ''
        if txt and not txt.startswith('<'):
          nuser+=1
          if first is None:first=txt[:160].replace('\n',' ')
      if d.get('type')=='assistant':
        m=d.get('message',{});u=m.get('usage');mid=m.get('id')
        if u and mid: seen[mid]=(m.get('model'),u)
    tok=collections.Counter()
    for mid,(mo,u) in seen.items():
      models[mo]+=1
      for k in ('input_tokens','cache_creation_input_tokens','cache_read_input_tokens','output_tokens'):
        tok[k]+=u.get(k,0) or 0
    rows.append(dict(f=f.replace(r,os.path.basename(r)[-12:]),sub='/subagents/' in f,start=min(ts) if ts else '',end=max(ts) if ts else '',calls=len(seen),models=dict(models),nuser=nuser,first=first,entry=list(entry),size=os.path.getsize(f),**tok))
json.dump(rows,open(sys.argv[1],'w'),indent=0)
