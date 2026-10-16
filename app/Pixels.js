// 4 колонки x 5 рядов; лесенка растёт снизу вверх, слева направо
export default function Pixels({px=16}){const m=['','','','p1','','','p2','p2','','p3','p3','p3','p4','p4','p4','p4','p5','p5','p5','p5'];
 return <div className="pixels pix-anim" style={{'--cols':4,'--px':px+'px'}} aria-hidden="true">{m.map((c,i)=>{const row=Math.floor(i/4),col=i%4;const step=(4-row)*2+col*0.6;return <i key={i} className={c} style={c?{'--s':step}:undefined}/>})}</div>}
