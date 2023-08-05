<template>
    <div class="bg-zinc-950 min-h-screen max-h-full flex flex-col gap-6 text-white p-5 justify-between">
        <HomeNavbar />
        <main class="text-start flex flex-col gap-8 p-10">
            <section class="flex flex-col gap-5">
                <span>
                    <h1 class="text-5xl font-semibold">
                        {{ article.title }}
                    </h1>
                </span>

                <div class="flex gap-4 flex-wrap" v-if="!isEmpty(article.tags)">
                    <a :href="`#${tag.slug}`" v-for="tag in article.tags" class="text-white bg-gradient-to-r from-emerald-500 to-teal-600 rounded-lg p-1 text-sm">
                        #{{ tag.name }}
                    </a>
                </div>

                <span class="flex gap-3 text-base text-zinc-300">
                    <h3 class="" style="direction: rtl">
                        {{ jmoment(article.updated_at).format("jMMMM jD , jYYYY") }}
                        Published
                    </h3>
                    <h3 class="text-emerald-500">|</h3>
                    <h3 class="">10 mean read</h3>
                </span>
            </section>

            <section class="flex flex-col md:flex-row-reverse gap-5 h-full w-full">
                <aside class="w-full md:w-1/3 sticky right-0 top-28 h-fit" v-if="!isEmpty(article.toc)">
                    <TableOfContents :toc="article.toc" />
                </aside>
                <div class="w-full">
                    <VueShowdown flavor="github" :markdown="article.article"  />
                </div>
            </section>
        </main>
        <Footer />
    </div>
</template>

<script lang="ts">
    import HomeNavbar from '@/components/HomeNavbar.vue';
    import { defineComponent } from 'vue';
    import TableOfContents from '@/components/TableOfContents.vue';
    import hljs from 'highlight.js';
    import 'highlight.js/styles/github-dark.css';
    import isEmpty from 'lodash/isEmpty';
    // @ts-ignore
    import { VueShowdown } from 'vue-showdown';
    import { mapState, mapActions } from 'vuex';
    // @ts-ignore
    import jmoment from 'moment-jalaali';
    // @ts-ignore
    import moment from 'moment';
    // @ts-ignore
    import fa from 'moment/locale/fa';
    import Footer from '@/components/Footer.vue';
    import { blogInterface } from '@/store';

    export default defineComponent({
        name: 'ArticleView',
        components: {
            HomeNavbar,
            Footer,
            TableOfContents,
            VueShowdown
        },
        setup() {
            moment.updateLocale("fa", fa);
            jmoment.loadPersian({dialect: "persian-modern"});
            return {
                isEmpty,
                jmoment
            }
        },
        computed: {
            ...mapState(["articles"]),
            article() {
                const articlesArr: Array<blogInterface> = this.articles;
                return articlesArr.length > 0 ? articlesArr[0] : Object()
            }
        },
        methods: {
            ...mapActions(["get_article"])
        },
        mounted() {
            hljs.highlightAll()
        },
        async beforeMount() {
            await this.get_article(this.$route.params.slug);
            document.title = this.article.title
        }
    })
</script>