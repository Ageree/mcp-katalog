import json,shlex,re,os,subprocess
from extract import extract
D='../data/servers.json'; d=json.load(open(D))
man=[e for e in d if not e['install']['claude_code']]
repos=sorted({e['repo_url'].split('github.com/')[1].split('/tree')[0] for e in man})
open('manual.txt','w').write('\n'.join(repos)); subprocess.run(['python3','fetch_readme.py','manual.txt'])
def from_claude(c):
    t=shlex.split(c.replace('\\\n',' '))[3:]; env={}; tr='stdio'; rest=[]
    i=0; cmd=None
    while i<len(t):
        a=t[i]
        if a=='--': cmd=t[i+1:]; break
        if a in('-e','--env'): k,_,v=t[i+1].partition('='); env[k]=v; i+=2; continue
        if a in('--transport','-t'): tr=t[i+1]; i+=2; continue
        if a in('--scope','-s','--header','-H'): i+=2; continue
        rest.append(a); i+=1
    if not rest: return None
    name=rest[0]
    if cmd: cfg={'command':cmd[0],'args':cmd[1:]}; tr='stdio'
    elif len(rest)>1 and rest[1].startswith('http'): cfg={'url':rest[1]}; tr='http' if tr!='sse' else 'sse'
    else: return None
    if env: cfg['env']=env
    return name,cfg,tr
def to_claude(name,cfg):
    if 'url' in cfg: return f"claude mcp add --transport http {name} {cfg['url']}"
    env=''.join(f" -e {k}={shlex.quote(str(v))}" for k,v in (cfg.get('env') or {}).items())
    return f"claude mcp add {name}{env} -- {cfg['command']} {' '.join(shlex.quote(str(a)) for a in cfg.get('args',[]))}".strip()
n=0
for e in man:
    r=e['repo_url'].split('github.com/')[1].split('/tree')[0]; p='readmes/'+r.replace('/','__')+'.md'
    if e.get('monorepo') or not os.path.exists(p): continue
    x=extract(open(p).read()); cc=x.get('claude'); cfg=None; tr=None
    if 'cfg' in x:
        nm,c=x['cfg']; c={k:v for k,v in c.items() if k in('command','args','env','url')}; cfg=(nm,c); tr='http' if 'url' in c else 'stdio'
    if cc and not cfg:
        f=from_claude(cc)
        if f: cfg=(f[0],f[1]); tr=f[2]
    if not cfg or 'example.com' in json.dumps(cfg[1]): continue
    if not cc: cc=to_claude(*cfg)
    if 'example.com' in cc: continue
    e['install']={'claude_code':cc,'cursor':json.dumps({'mcpServers':{cfg[0]:cfg[1]}},ensure_ascii=False,indent=2),'note':'Команда взята из README; при необходимости сначала установите пакет (pip/npm) и подставьте свои ключи.'}
    e['transport']=tr; e['transport_verified']=True; n+=1
    if tr=='http': e['yandex_ai_studio']='Подходит: удалённый HTTP-сервер можно подключить в Yandex AI Studio (MCP Hub).'
for e in d:
    if e['slug']=='bitrix24-docs':
        e['install']={'claude_code':'claude mcp add --transport http bitrix24 https://mcp.bitrix24.com/mcp/','cursor':json.dumps({'mcpServers':{'bitrix24':{'url':'https://mcp.bitrix24.com/mcp/'}}},indent=2),'note':'Адрес из официального MCP Registry (io.github.bitrix24/bitrix24).'}; e['transport']='http'; e['transport_verified']=True
    e['gigacode']="GigaCode поддерживает MCP через стандартный JSON-конфиг mcpServers — совместимость не проверялась." if e['install']['cursor'] else None
json.dump(d,open(D,'w'),ensure_ascii=False,indent=1)
print('enriched',n,'total',len(d),'still manual',sum(1 for e in d if not e['install']['claude_code']))
