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
    images: [],
    slug: string,
    technologies: [],
    started_at: string,
    ended_at: string,
}

export default createStore({
    state: {
        cv: {
            about: "",
            image: "",
            location: "",
        },
        projects: {
            name: "",
            explanations: "",
            images: [],
            slug: "",
            technologies: [],
            started_at: "",
            ended_at: ""
        },
    },
    getters: {},
    mutations: {
        UPDATE_CV(state, payload: cvInterface) {
            state.cv.about = payload.about
            state.cv.image = payload.image
            state.cv.location = payload.location
        },
        UPDATE_PROJECTS(state, payload: projectsInterface) {
            state.projects.name = payload.name
            state.projects.explanations = payload.explanations
            state.projects.images = payload.images
            state.projects.slug = payload.slug
            state.projects.technologies = payload.technologies
            state.projects.started_at = payload.started_at
            state.projects.ended_at = payload.ended_at
        }
    },
    actions: {
        async update_cv({ commit }) {
            const url = "/api/v1/cv";
            const res = await axios.get(url)
            if (res.status === 200) commit("UPDATE_CV", res.data[0])
        },
        async update_projects({ commit }) {
            const url = "/api/v1/project"
            const res = await axios.get(url)
            if (res.status === 200) commit("UPDATE_PROJECTS", res.data)
        }
    },
    modules: {},
});
