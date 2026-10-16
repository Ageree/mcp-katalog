import { servicePages } from '../../../lib/data'; import List from '../../List';
export const dynamicParams=false;
export function generateStaticParams(){return servicePages.map(p=>({svc:p.slug}))}
const get=async p=>{const x=await p;return servicePages.find(s=>s.slug===x.svc)};
export async function generateMetadata({params}){const p=await get(params);return {title:`MCP-сервер для ${p.name} — ${p.items.length} вариантов для Claude Code и Cursor`,description:`Каталог MCP-серверов для ${p.name}: официальные и от сообщества, с командами установки для Claude Code, Cursor и Yandex AI Studio.`}}
export default async function Page({params}){const p=await get(params);const off=p.items.filter(s=>s.official).length;
 return <List crumbs="Сервисы" eyebrow={`Сервис · ${p.items.length} серверов${off?` · официальных: ${off}`:''}`} title={`MCP-сервер для ${p.name}`} lead={`Подключите ${p.name} к Claude Code, Cursor или другому ИИ-ассистенту. Ниже — все найденные серверы, отсортированные по звёздам GitHub.`} items={p.items}/>}
