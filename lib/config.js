// Приём заявок «Добавить сервер» — без платных сервисов и без бэкенда.
// SUBMIT_GITHUB_REPO: публичный репозиторий "owner/repo" — форма откроет предзаполненный GitHub issue (метка submission).
// SUBMIT_EMAIL: запасной вариант — mailto с готовым письмом.
// Если оба пустые — форма формирует готовую заявку и даёт её скопировать.
export const SUBMIT_GITHUB_REPO = process.env.NEXT_PUBLIC_SUBMIT_REPO || 'Ageree/mcp-katalog';
export const SUBMIT_EMAIL = process.env.NEXT_PUBLIC_SUBMIT_EMAIL || '';
