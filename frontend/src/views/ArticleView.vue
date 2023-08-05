<template>
    <div class="bg-zinc-950 min-h-screen max-h-full flex flex-col gap-6 text-white p-5 justify-between">
        <HomeNavbar />

        <main class="flex flex-col gap-3">
            
        </main>

        <Footer />
    </div>
</template>

<script lang="ts">
    import HomeNavbar from '@/components/HomeNavbar.vue';
    import { defineComponent } from 'vue';
    import { mapState, mapActions } from 'vuex';
    import Footer from '@/components/Footer.vue';
    import { blogInterface } from '@/store';

    export default defineComponent({
        name: 'ArticleView',
        components: {
            HomeNavbar,
            Footer
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
        async created() {
            await this.get_article(this.$route.params.slug);
            document.title = `Article: ${this.article.title}`
        }
    })
</script>