export default interface blogInterface {
    title: string,
    tags: Array<string>,
    user: {first_name: string, last_name: string, picture: string},
    article?: string,
    updated_at: string,
    created_at?: string,
    thumbnail: string
}