import axios from 'axios';


export default {
    state: {
        projects: [],
    },
    mutations: {
        UPDATE_PROJECTS(state, payload) {
            state.projects = payload;
        },
    },
    actions: {
        async update_projects({ commit }) {
            const url = "/api/v1/project";
            const res = await axios.get(url);
            if (res.status === 200) commit("UPDATE_PROJECTS", res.data);
        }
    },
}