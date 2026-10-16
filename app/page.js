import { all, categories, fresh, servicePages } from '../lib/data';
import Catalog from './Catalog'; import Card from './Card'; import Pixels from './Pixels'; import Arc from './Arc';
export default function Home(){const off=all.filter(s=>s.official).length;return <>
 <section className="hero"><Arc size={520} style={{left:-260,top:-300}}/><Arc size={900} delay={0.4} style={{right:-450,top:-500}}/><Arc size={300} delay={0.8} style={{right:120,top:-170}}/>
  <div className="eyebrow">01 · Каталог · {all.length} серверов</div>
  <h1 className="display" style={{marginTop:16}}>MCP-серверы<br/><span className="brand-text">для российских сервисов</span></h1>
  <p className="lead">Ozon, Wildberries, Яндекс, 1С, Битрикс24, GigaChat, Т-Банк и ещё десятки сервисов — с готовыми командами для Claude Code и Cursor. Официальных серверов: {off}.</p>
  <div className="stack" style={{marginTop:32}}><a className="btn btn-brand btn-lg" href="#catalog">Смотреть каталог →</a><a className="btn btn-secondary btn-lg" href="/add/">Добавить сервер</a></div>
  <div className="pix"><Pixels/></div></section>
 <div className="stripes flow" style={{height:24}}/>
 <div className="sec-head" id="new"><div><div className="eyebrow">02 · Новое</div><h2 style={{marginTop:8}}>Недавно добавленные</h2></div></div>
 <div className="grid">{fresh.map(s=><Card key={s.slug} s={s}/>)}</div>
 <div className="sec-head" id="services"><div><div className="eyebrow">03 · Сервисы</div><h2 style={{marginTop:8}}>MCP для популярных сервисов</h2></div></div>
 <div className="chips">{servicePages.map(p=><a key={p.slug} className="chip" href={`/mcp/${p.slug}/`}>{p.name} <span className="n">{p.items.length}</span></a>)}</div>
 <div className="sec-head" id="categories"><div><div className="eyebrow">04 · Категории</div><h2 style={{marginTop:8}}>Категории</h2></div></div>
 <div className="chips">{categories.map(c=><a key={c.slug} className="chip" href={`/category/${c.slug}/`}>{c.name} <span className="n">{c.count}</span></a>)}</div>
 <div className="sec-head" id="catalog"><div><div className="eyebrow">05 · Все серверы</div><h2 style={{marginTop:8}}>Весь каталог</h2></div></div>
 <Catalog servers={all} categories={categories}/></>}
