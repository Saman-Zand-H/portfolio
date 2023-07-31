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

export default createStore({
    state: {
        cv: {
            about: "",
            image: "",
            location: ""
        },
        projects: new Array<projectsInterface>(),
    },
    getters: {},
    mutations: {
        UPDATE_CV(state, payload: cvInterface) {
            state.cv.about = payload.about
            state.cv.image = payload.image
            state.cv.location = payload.location
        },
        UPDATE_PROJECTS(state, payload: Array<projectsInterface>) {
            state.projects = payload
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
