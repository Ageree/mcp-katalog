import { all, catSlug } from '../../../lib/data'; import Pixels from '../../Pixels'; import Hosting from '../../Hosting';
export const dynamicParams=false;
export function generateStaticParams(){return all.map(s=>({slug:s.slug}))}
const get=async p=>{const x=await p;return all.find(s=>s.slug===x.slug)};
export async function generateMetadata({params}){const s=await get(params);return {title:`MCP-сервер для ${s.service} — ${s.name} | установка в Claude Code и Cursor`,description:s.description_ru}}
export default async function Page({params}){const s=await get(params);
 return <><section className="hero"><div className="crumbs"><a href="/">Каталог</a> / <a href={`/category/${catSlug(s.category)}/`}>{s.category}</a></div>
 <div className="stack">{s.official?<span className="badge badge-brand">Официальный</span>:<span className="badge">Сообщество</span>}<span className="badge badge-info">{s.transport}</span>{s.install.claude_code&&<span className="badge badge-success">Готовая команда</span>}</div>
 <h1 className="h1" style={{marginTop:16}}>MCP-сервер для {s.service}</h1><p className="lead"><b>{s.name}.</b> {s.description_ru}</p>
 <div className="stack" style={{marginTop:24}}><a className="btn btn-primary" href={s.repo_url} rel="nofollow noopener">Репозиторий на GitHub →</a></div><div className="pix"><Pixels px={12}/></div></section>
 <div className="stripe-bar"/>
 <div className="two"><div><div className="eyebrow">01 · Установка</div><h2 className="h2" style={{margin:'8px 0 24px'}}>Как подключить</h2>
 {s.install.claude_code?<><div className="label" style={{marginBottom:8}}>Claude Code</div><pre className="code">{s.install.claude_code}</pre><div className="label" style={{marginBottom:8}}>Cursor · ~/.cursor/mcp.json</div><pre className="code">{s.install.cursor}</pre></>:<div className="alert">Готовой команды пока нет. {s.install.note} <a href={s.repo_url}>Открыть README →</a></div>}
 {s.install.note&&s.install.claude_code&&<div className="alert">{s.install.note}</div>}
 {s.yandex_ai_studio&&<p style={{fontSize:14}}><b>Yandex AI Studio:</b> {s.yandex_ai_studio}</p>}
 {s.gigacode&&<p className="muted" style={{fontSize:13}}><b>GigaCode:</b> {s.gigacode}</p>}</div>
 <div><div className="eyebrow">02 · Сведения</div><table className="kv" style={{marginTop:16}}><tbody>
 <tr><td>Сервис</td><td>{s.service}</td></tr><tr><td>Категория</td><td>{s.category}</td></tr>
 <tr><td>Статус</td><td>{s.official?'Официальный (от вендора)':'Сообщество'}</td></tr>
 <tr><td>Транспорт</td><td>{s.transport}{!s.transport_verified&&' (предположительно)'}</td></tr>
 <tr><td>Язык</td><td>{s.language||'—'}</td></tr><tr><td>Лицензия</td><td>{s.license||'—'}</td></tr>
 <tr><td>Звёзды GitHub</td><td>★ {s.stars}{s.monorepo&&' (весь репозиторий)'}</td></tr>
 <tr><td>Последний push</td><td>{s.last_commit}</td></tr></tbody></table></div></div>
 {s.transport!=='http'?<Hosting/>:<Hosting compact llmOnly/>}</>}
