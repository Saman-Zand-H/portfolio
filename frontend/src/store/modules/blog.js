import axios from 'axios';


const blogModule = {
    namespaced: false,
    state: {
        articles: [],
    },
    mutations: {
        UPDATE_ARTICLES(state, payload) {
            state.articles = payload;
        },
    },
    actions: {
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
                                tags,
                            }
                        }
                    }
                }`,
            };
            const res = await axios.post(endpoint, query);
            if (res.status === 200) {
                const articles = res?.data?.data?.articles?.edges?.map(
                    (v) => v.node
                );
                commit("UPDATE_ARTICLES", articles);
            }
        },
        async update_articles(
            { commit },
            article = false,
            page = 1,
            count = 8
        ) {
            const endpoint = "graphql/v1/";
            const query = {
                query: `{
                    articles(offset: ${count * (page - 1)}, first: ${count}) {
                        edges {
                            node {
                                thumbnail,
                                title,
                                subtitle,
                                slug,
                                tags,
                                ${article ? "article" : ""}
                            }
                        }
                    }
                }`,
            };
            const res = await axios.post(endpoint, query);
            if (res.status === 200) {
                const articles = res?.data?.data?.articles?.edges?.map(
                    (v) => v.node
                );
                commit("UPDATE_ARTICLES", articles);
            }
        },
    },
};

export default blogModule