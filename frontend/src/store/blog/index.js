import axios from 'axios';
import { createStore } from "vuex";


export default createStore({
    state: {
        articles: []
    },
    mutations: {
        UPDATE_ARTICLES(state, payload) {
            state.articles = payload
        }
    },
    actions: {

    }
})