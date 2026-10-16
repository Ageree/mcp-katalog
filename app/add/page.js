'use client';
import { useState } from 'react';
import Arc from '../Arc';
import { SUBMIT_GITHUB_REPO, SUBMIT_EMAIL } from '../../lib/config';
export default function Add(){const [text,setText]=useState('');const [copied,setCopied]=useState(false);
 function onSubmit(e){e.preventDefault();const f=Object.fromEntries(new FormData(e.target));
  const title=`Новый сервер: ${f.service||f.repo}`;
  const body=`**Репозиторий:** ${f.repo}\n**Сервис:** ${f.service||'—'}\n**Официальный:** ${f.official?'да':'нет/не знаю'}\n**Команда установки:** ${f.install||'—'}\n\n**Описание:**\n${f.desc||'—'}\n\n**Контакт:** ${f.email||'—'}\n\n_Отправлено с формы MCP·Каталог_`;
  if(SUBMIT_GITHUB_REPO){window.open(`https://github.com/${SUBMIT_GITHUB_REPO}/issues/new?labels=submission&title=${encodeURIComponent(title)}&body=${encodeURIComponent(body)}`,'_blank','noopener');setText(body);return}
  if(SUBMIT_EMAIL){window.location.href=`mailto:${SUBMIT_EMAIL}?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(body)}`;setText(body);return}
  setText(`# ${title}\n\n${body}`)}
 return <><section className="hero"><Arc size={600} style={{right:-300,top:-380}}/><div className="eyebrow">Модерация · 24 часа</div><h1 className="h1" style={{marginTop:12}}>Добавить сервер</h1><p className="lead">Знаете MCP-сервер для российского сервиса? Пришлите его — мы проверим и добавим в каталог.</p></section><div className="stripe-bar"/>
 <div className="pad" style={{paddingTop:48}}>
 <form className="form" onSubmit={onSubmit}>
 <div className="field"><label className="label">Ссылка на репозиторий *</label><input name="repo" className="input" required type="url" placeholder="https://github.com/…"/><span className="hint">GitHub, GitVerse или GitFlic</span></div>
 <div className="field"><label className="label">Сервис *</label><input name="service" required className="input" placeholder="Например: Ozon Seller API"/></div>
 <div className="field"><label className="label">Команда установки</label><input name="install" className="input" placeholder="npx -y …"/></div>
 <div className="field"><label className="label">Описание</label><textarea name="desc" className="input" rows="4"/></div>
 <label className="label" style={{display:'flex',gap:8,alignItems:'center'}}><input type="checkbox" name="official"/> Я представляю вендора (официальный сервер)</label>
 <div className="field"><label className="label">Email для связи</label><input name="email" className="input" type="email"/></div>
 <div><button className="btn btn-brand btn-lg">{SUBMIT_GITHUB_REPO?'Открыть заявку на GitHub →':SUBMIT_EMAIL?'Отправить письмом →':'Сформировать заявку'}</button></div></form>
 {text&&<div style={{marginTop:32,maxWidth:640}}><div className="alert">{SUBMIT_GITHUB_REPO?'Мы открыли предзаполненный issue на GitHub — осталось нажать «Submit new issue». Текст заявки ниже на случай, если окно не открылось.':SUBMIT_EMAIL?'Открылся почтовый клиент с готовым письмом. Текст заявки ниже.':'Заявка сформирована. Скопируйте её — приём заявок через GitHub скоро будет подключён.'}</div>
 <pre className="code" style={{marginTop:16}}>{text}</pre><button className="btn btn-secondary" onClick={()=>{navigator.clipboard.writeText(text);setCopied(true)}}>{copied?'Скопировано ✓':'Скопировать заявку'}</button></div>}
 </div></>}
