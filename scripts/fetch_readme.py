import json,urllib.request,sys,os,concurrent.futures as cf
m=json.load(open('meta.json'))
for f in ['gh.json','gh2.json']:
    if os.path.exists(f):
        for k,v in json.load(open(f)).items(): m.setdefault(k.lower(),v)
want=[l.strip() for l in open(sys.argv[1]) if l.strip()]
def get(r):
    p='readmes/'+r.replace('/','__')+'.md'
    if os.path.exists(p): return
    d=m.get(r.lower(),{}); b=d.get('default_branch','main')
    for name in ['README.md','readme.md','README.ru.md','Readme.md']:
        try:
            t=urllib.request.urlopen(f"https://raw.githubusercontent.com/{r}/{b}/{name}",timeout=20).read().decode('utf8','ignore'); open(p,'w').write(t); return
        except Exception: pass
with cf.ThreadPoolExecutor(16) as ex: list(ex.map(get,want))
