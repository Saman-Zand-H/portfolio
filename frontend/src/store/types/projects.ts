export default interface projectsInterface {
    name: string;
    explanations: string;
    images: Array<{ image: string; alt: string }>;
    slug: string;
    technologies: Array<{ icon: string; name: string; url: string }>;
    started_at: string;
    ended_at: string;
}
