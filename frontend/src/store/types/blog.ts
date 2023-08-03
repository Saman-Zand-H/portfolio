export default interface blogInterface {
    title: string,
    subtitle: string,
    thumbnail: string,
    tags: Array<string>,
    slug: string,
    created_at?: string,
    article?: string,
    updated_at: string,
    count: number
}