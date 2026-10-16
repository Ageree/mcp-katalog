import './globals.css';
import Newsletter from './Newsletter';
import { categories, servicePages, all } from '../lib/data';
export const metadata = { title: 'MCP·Каталог — MCP-серверы для российских сервисов', description: 'Русскоязычный каталог MCP-серверов: Ozon, Wildberries, Яндекс, 1С, Битрикс24, GigaChat и другие. Инструкции установки для Claude Code и Cursor.' };
export default function RootLayout({ children }) {
  return (<html lang="ru"><body>
    <nav className="nav"><a className="logo" href="/"><span style={{width:14,height:14,background:'var(--stripes)',display:'inline-block'}}/>MCP·Каталог</a>
      <a href="/#catalog" className="hide-m">Серверы</a><a href="/#categories" className="hide-m">Категории</a><a href="/#services" className="hide-m">Сервисы</a><a href="/#new" className="hide-m">Новое</a><span className="spacer"/><a className="nav-cta" href="/add/">Добавить сервер</a></nav>
    <div className="container">{children}</div>
    <footer className="footer"><div className="stripes" style={{height:12}}/>
      <div className="footer-grid"><div><b style={{fontSize:16}}>MCP·Каталог</b><p style={{opacity:.7,maxWidth:340}}>Независимый русскоязычный каталог MCP-серверов: {all.length} серверов для российских и мировых сервисов.</p><Newsletter/></div>
        <div><h4>Категории</h4><ul>{categories.slice(0,6).map(c=><li key={c.slug}><a href={`/category/${c.slug}/`}>{c.name}</a></li>)}</ul></div>
        <div><h4>Сервисы</h4><ul>{servicePages.slice(0,6).map(p=><li key={p.slug}><a href={`/mcp/${p.slug}/`}>MCP для {p.name}</a></li>)}</ul></div>
        <div><h4>Проект</h4><ul><li><a href="/add/">Добавить сервер</a></li><li><a href="/#new">Новое</a></li><li><a href="https://modelcontextprotocol.io" rel="nofollow">Что такое MCP</a></li></ul></div></div>
      <div className="footer-bottom"><span>© 2026 MCP·Каталог</span><span>Данные: GitHub, MCP Registry, Yandex Cloud Marketplace</span></div></footer>
  </body></html>);
}
