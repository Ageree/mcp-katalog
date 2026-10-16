'use client';
import { useState, useMemo } from 'react';
import Card from './Card';
export default function Catalog({servers,categories}){const [q,setQ]=useState('');const [cat,setCat]=useState('');const [off,setOff]=useState(false);
 const list=useMemo(()=>{const t=q.toLowerCase().trim();return servers.filter(s=>(!cat||s.category===cat)&&(!off||s.official)&&(!t||[s.name,s.description_ru,s.service,s.slug].join(' ').toLowerCase().includes(t))).sort((a,b)=>b.stars-a.stars)},[q,cat,off,servers]);
 return <div><div className="pad" style={{paddingBottom:24}}><div className="search" style={{maxWidth:640}}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input className="input" placeholder="Поиск: Ozon, 1С, Метрика, Telegram…" value={q} onChange={e=>setQ(e.target.value)}/><kbd>{list.length}</kbd></div></div>
 <div className="chips"><button className={'chip '+(!cat?'on':'')} onClick={()=>setCat('')}>Все <span className="n">{servers.length}</span></button>
 {categories.map(c=><button key={c.slug} className={'chip '+(cat===c.name?'on':'')} onClick={()=>setCat(cat===c.name?'':c.name)}>{c.name} <span className="n">{c.count}</span></button>)}
 <button className={'chip '+(off?'on':'')} onClick={()=>setOff(!off)}>Только официальные</button></div>
 <div className="grid" style={{borderTop:0}}>{list.map(s=><Card key={s.slug} s={s}/>)}</div></div>}
