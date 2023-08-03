<template>
    <div class="bg-zinc-950 text-white max-h-full min-h-screen w-full p-5">
        <HomeNavbar />
        <div class="p-5 w-full md:w-3/4 my-14 mx-auto text-left">
            <span class="my-5 flex flex-col gap-5">
                <h3 class="text-2xl">Hi, I'm</h3>
                <h1 class="text-4xl font-semibold">Saman Zand Haghighi</h1>
                <h4 class="text-lg text-gray-400">
                    I'm a Full-Stack Developer.
                </h4>
                <h4 class="text-lg text-gray-400">
                    I work with Javascript, Typescript and Python frameworks. 
                    I'm also open-source contributor.
                </h4>
                <span class="flex gap-20 text-gray-400">
                    <a href="https://github.com/saman-zand-h/" class="flex items-center gap-3 hover:text-gray-400/80 transition-colors duration-200">
                        <i class="fa fab fa-github text-3xl"></i>
                        GitHub
                    </a>
                    <a href="https://linkedin.com/in/saman-zand-h" class="flex items-center gap-3 hover:text-gray-400/80 transition-colors duration-200">
                        <i class="fa fab fa-linkedin text-3xl"></i>
                        LinkedIn
                    </a>
                </span>
            </span>
            <div class="my-14 flex flex-col gap-5">
                <span>
                    <h2 class="text-3xl">
                        Recently Published
                    </h2>
                </span>
                <div class="">
                    <BlogPortfolioCard v-for="article in articles" :article="article" />
                </div>
                <div v-if="pages > 1">
                    <Paginator @page-changed="changePage" :pages="pages" />
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@700&display=swap');

* {
    font-family: 'Space Mono', monospace
}
</style>

<script lang="ts">
    import { defineComponent } from 'vue';
    import { mapState, mapActions } from 'vuex';
    import HomeNavbar from '@/components/HomeNavbar.vue';
    import Paginator from '@/components/Paginator.vue';
    import BlogPortfolioCard from '@/components/BlogPortfolioCard.vue';
    import { toInteger, toNumber } from 'lodash';

    export default defineComponent({
        name: 'ArticlesListView',
        components: {
            BlogPortfolioCard,
            HomeNavbar,
            Paginator
        },
        computed: {
            ...mapState(["articles", "articles_count"]),
            pages(): number {
                // number of articles in each page
                const count = 8;
                return Math.ceil(toNumber(this.articles_count) / count)
            }
        },
        methods: {
            ...mapActions(["update_articles"]),
            async changePage(value: number) {
                this.$router.push({query: {page: value}});
                await this.update_articles({page: value})
            }
        },
        async created() {
            const page = this.$route.query.page
            await this.update_articles({page: page ? toInteger(page) : 1})
        },
    })
</script>