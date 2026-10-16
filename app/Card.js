const ini=s=>s.name.replace(/[^A-Za-zА-Яа-я0-9]/g,'').slice(0,2).toUpperCase();
export default function Card({s}){return <a className="card" href={`/server/${s.slug}/`}><div style={{display:'flex',gap:12,alignItems:'center',justifyContent:'space-between'}}><div className="card-icon">{ini(s)}</div>{s.official?<span className="badge badge-brand">Официальный</span>:<span className="badge">Сообщество</span>}</div>
<h3 className="h3">{s.name}</h3><p>{s.description_ru}</p>
<div className="card-meta"><span>★ {s.stars}</span><span>{s.transport}{s.language?' · '+s.language:''}</span>{s.install.claude_code&&<span>⚡ 1 команда</span>}</div></a>}
