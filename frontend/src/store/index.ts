import { createStore } from "vuex";
import axios from 'axios';

export interface cvInterface {
    about: string,
    image: string,
    location: string
}

export interface projectsInterface {
    name: string,
    explanations: string,
    images: Array<{image: string, alt: string}>,
    slug: string,
    technologies: Array<{icon: string, name: string, url: string}>,
    started_at: string,
    ended_at: string,
}


export interface blogInterface {
    title: string,
    subtitle: string,
    thumbnail: string,
    tags: Array<string>,
    slug: string,
    created_at?: string,
    article?: string,
    updated_at: string
}

export default createStore({
    state: {
        cv: {
            about: "",
            image: "",
            location: "",
        },
        projects: new Array<projectsInterface>(),
        technologies: new Array<{ name: string; image: string; url: string }>(),
        articles: new Array<blogInterface>()
    },
    getters: {},
    mutations: {
        UPDATE_CV(state, payload: cvInterface) {
            state.cv.about = payload.about;
            state.cv.image = payload.image;
            state.cv.location = payload.location;
        },
        UPDATE_PROJECTS(state, payload: Array<projectsInterface>) {
            state.projects = payload;
        },
        UPDATE_TECHNOLOGIES(
            state,
            payload: Array<{
                name: string;
                image: string;
                url: string;
            }>
        ) {
            state.technologies = payload;
        },
        UPDATE_ARTICLES(state, payload: Array<blogInterface>) {
            state.articles = payload
        }
    },
    actions: {
        async update_cv({ commit }) {
            const url = "/api/v1/cv";
            const res = await axios.get(url);
            if (res.status === 200) commit("UPDATE_CV", res.data[0]);
        },
        async update_projects({ commit }) {
            const url = "/api/v1/project";
            const res = await axios.get(url);
            if (res.status === 200) commit("UPDATE_PROJECTS", res.data);
        },
        async update_technologies({ commit }) {
            const url = "/api/v1/technology";
            const res = await axios.get(url);
            if (res.status === 200) commit("UPDATE_TECHNOLOGIES", res.data);
        },
        async get_preview({ commit }, count = 3) {
            const endpoint = "/graphql/v1/";
            const query = {
                query: `{
                    articles(first: ${count}) {
                        edges {
                            node {
                                thumbnail,
                                title,
                                subtitle,
                                slug,
                            }
                        }
                    }
                }`
            };
            const res = await axios.post(endpoint, query);
            if (res.status === 200) {
                const articles = res
                                    ?.data
                                    ?.data
                                    ?.articles
                                    ?.edges
                                    ?.map((v: {node: blogInterface}) => v.node)
                commit("UPDATE_ARTICLES", articles);
            }
        },
    },
});
