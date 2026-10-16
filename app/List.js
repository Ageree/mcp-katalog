import Arc from './Arc';
import Card from './Card'; import Pixels from './Pixels';
export default function List({eyebrow,title,lead,items,crumbs}){return <><section className="hero"><Arc size={600} style={{right:-300,top:-380}}/><div className="crumbs"><a href="/">Каталог</a> / {crumbs}</div><div className="eyebrow">{eyebrow}</div><h1 className="h1" style={{marginTop:12}}>{title}</h1><p className="lead">{lead}</p><div className="pix"><Pixels px={12}/></div></section><div className="stripe-bar"/><div className="grid" style={{borderTop:0}}>{items.map(s=><Card key={s.slug} s={s}/>)}</div></>}
