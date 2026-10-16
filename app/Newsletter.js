'use client';
import { useState } from 'react';
export default function Newsletter(){const [ok,setOk]=useState(false);
 return <div style={{marginTop:24}}><h4>Рассылка</h4><p style={{opacity:.7,margin:'0 0 12px'}}>Раз в неделю — новые MCP-серверы для российских сервисов.</p>
 {ok?<p className="mono" style={{color:'var(--c-yellow-500)'}}>Спасибо! (заглушка — подписка пока не сохраняется)</p>:<form className="news" onSubmit={e=>{e.preventDefault();setOk(true)}}><input className="input" type="email" required placeholder="you@example.ru"/><button className="btn btn-brand">Подписаться</button></form>}</div>}
