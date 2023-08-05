<template>
    <div class="bg-zinc-950 min-h-screen max-h-full flex flex-col gap-6 text-white p-5 justify-between">
        <HomeNavbar />
        <article class="text-start flex flex-col gap-8 p-10">
            <header class="flex flex-col gap-5">
                <span>
                    <h1 class="text-5xl font-semibold">
                        {{ article.title }}
                    </h1>
                </span>

                <div class="flex gap-4 flex-wrap" v-if="!isEmpty(article.tags)">
                    <a :href="`#${JSON.parse(tag).slug}`" v-for="tag in article.tags" class="text-white bg-gradient-to-r from-emerald-500 to-teal-600 rounded-lg p-1 text-sm">
                        #{{ JSON.parse(tag).slug }}
                    </a>
                </div>

                <span class="flex gap-3 text-base text-zinc-300">
                    <h3 class="" style="direction: rtl">
                        {{ jmoment(article.updated_at).format("jMMMM jD , jYYYY") }}
                        Published
                    </h3>
                    <h3 class="text-emerald-400">|</h3>
                    <h3 class="">{{ calculatReadingTime() }} min. read</h3>
                </span>
            </header>

            <section class="flex flex-col gap-10 xl:flex-row-reverse xl:gap-5 h-full w-full">
                <aside class="w-full xl:w-1/3 xl:sticky right-0 top-28 h-fit" v-if="!isEmpty(article.toc)">
                    <TableOfContents :toc="article.toc" />
                </aside>
                <div class="w-full" id="article">
                    <VueShowdown flavor="github" :markdown="article.article"  />
                </div>
            </section>
        </article>
        <Footer />
    </div>
</template>

<script lang="ts">
    import HomeNavbar from '@/components/HomeNavbar.vue';
    import { defineComponent } from 'vue';
    import TableOfContents from '@/components/TableOfContents.vue';
    import hljs from 'highlight.js';
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
            ...mapActions(["get_article"]),
            calculatReadingTime() {
                const articleElem = document.getElementById("article");
                const numWords = articleElem?.textContent?.split(" ").length || 0;
                const avgWPM = 300;
                return Math.ceil(numWords / avgWPM)
            }
        },
        updated() {
            hljs.highlightAll();
            document.title = this.article.title;
            const tocLinks = document.querySelectorAll(".toc-heading");
            const setActiveLink = () => {
                tocLinks.forEach((link) => {
                    const sectionId = link.getAttribute("href");
                    // @ts-ignore
                    const heading = document?.querySelector(sectionId);
                    const rect = heading?.getBoundingClientRect();

                    if (!rect) return

                    if (rect?.bottom >= 0 && rect?.top >= 0) {
                        link?.classList.remove("text-zinc-400")
                        link?.classList.add("text-emerald-500")
                    } else {
                        link?.classList.add("text-zinc-400")
                        link?.classList.remove("text-emerald-500")
                    }
                });
            };

            window.onscroll = setActiveLink;

        },
        async beforeMount() {
            await this.get_article(this.$route.params.slug);
        },
    })
</script>