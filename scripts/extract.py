import json,re,os,glob
def jload(s):
    s=re.sub(r'//[^\n"]*\n','\n',s); s=re.sub(r',(\s*[}\]])',r'\1',s)
    try: return json.loads(s)
    except Exception:
        try: return json.loads('{'+s+'}')
        except Exception: return None
GOOD=('npx','uvx','docker','bunx','pipx')
def extract(md):
    res={}
    for m in re.finditer(r'^[ \t]*(?:\$\s*)?(claude mcp add(?:[^\n]*\\[ \t]*\n)*[^\n]*)',md,re.M):
        c=re.sub(r'\\[ \t]*\n\s*',' ',m.group(1)).strip().strip('`')
        if not any(b in c for b in ('/path','/путь','python ','node ','uv run','localhost','127.0.0.1','--directory','.venv')): res['claude']=c; break
    for blk in re.findall(r'```(?:json|jsonc|JSON)?\s*\n(.*?)```',md,re.S):
        if '"command"' not in blk and '"url"' not in blk: continue
        j=jload(blk)
        if not isinstance(j,dict): continue
        servers=j.get('mcpServers') or j.get('servers') or (j.get('mcp',{}) or {}).get('servers') or j
        if not isinstance(servers,dict): continue
        for name,cfg in servers.items():
            if not isinstance(cfg,dict): continue
            if cfg.get('command') in GOOD or (cfg.get('url','').startswith('https://') and 'localhost' not in cfg.get('url','')):
                res['cfg']=(name,cfg); return res
    return res
if __name__=='__main__':
    for f in sorted(glob.glob('readmes/*.md')):
        r=extract(open(f).read())
        if r: print(os.path.basename(f), r.get('claude'), json.dumps(r.get('cfg'),ensure_ascii=False)[:160])
