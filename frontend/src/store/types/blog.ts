export default interface blogInterface {
    title: string;
    subtitle: string;
    thumbnail: string;
    tags: Array<{ name: string; slug: string }>;
    slug: string;
    created_at?: string;
    article?: string;
    updated_at: string;
    toc?: string;
}