import { all, categories } from '../../../lib/data'; import List from '../../List';
export const dynamicParams=false;
export function generateStaticParams(){return categories.map(c=>({cat:c.slug}))}
const get=async p=>{const x=await p;return categories.find(c=>c.slug===x.cat)};
export async function generateMetadata({params}){const c=await get(params);return {title:`MCP-серверы: ${c.name} — каталог для Claude и Cursor`,description:`${c.count} MCP-серверов в категории «${c.name}» с инструкциями по установке.`}}
export default async function Page({params}){const c=await get(params);const list=all.filter(s=>s.category===c.name).sort((a,b)=>b.stars-a.stars);
 return <List crumbs="Категории" eyebrow={`Категория · ${list.length} серверов`} title={`MCP-серверы: ${c.name}`} lead={`Сервисы: ${[...new Set(list.map(s=>s.service))].slice(0,14).join(', ')}.`} items={list}/>}
