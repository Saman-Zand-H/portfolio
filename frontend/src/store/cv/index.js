import axios from "axios";


export default {
    state: {
        cv: {
            about: "",
            image: "",
            location: "",
        },
    },
    mutations: {
        UPDATE_CV(state, payload) {
            state.cv.about = payload.about;
            state.cv.image = payload.image;
            state.cv.location = payload.location;
        },
    },
    actions: {
        async update_cv({ commit }) {
            const url = "/api/v1/cv";
            const res = await axios.get(url);
            if (res.status === 200) commit("UPDATE_CV", res.data[0]);
        }
    },
}