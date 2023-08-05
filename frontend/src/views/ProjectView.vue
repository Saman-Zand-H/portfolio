<template>
    <div class="min-h-screen max-h-full bg-zinc-950 p-5">
        <HomeNavbar />
        <main class="my-3 bg-zinc-800 text-white rounded-3xl py-6 px-9 flex flex-col gap-6 animate__animated animate__fadeInUp">
            <span class="text-5xl text-left font-semibold">
                {{ project?.name }}
            </span>
            <div class="rounded-3xl w-full md:w-1/2 m-auto p-3 bg-zinc-700/70">
                <swiper
                    :loop="true"
                    :navigation="true"
                    :pagination="{
                        clickable: true
                    }"
                    :modules="modules"
                    class="w-full"
                    >
                    <swiper-slide v-for="image in project?.images">
                        <img :src="image?.image" class="aspect-auto rounded-3xl">
                    </swiper-slide>
                </swiper>
            </div>
            <div class="text-left">
                <h2 class="text-3xl font-semibold">
                    Description
                </h2>
                <p class="px-5 text-right py-2" style="direction: rtl">
                    {{ project?.explanations }}
                </p>
            </div>
            <div class="text-left">
                <h2 class="text-3xl font-semibold">
                    Technologies
                </h2>
                <div class="flex flex-wrap gap-3 p-5 justify-center">
                    <a class="rounded-2xl flex flex-col items-center justify-center bg-zinc-100/20 p-2 hover:bg-zinc-100/10 transition-colors duration-200" v-for="technology in project?.technologies" :href="technology.url">
                        <img width="50" height="60" :src="technology.icon" :alt="technology.name">
                    </a>
                </div>
            </div>
            <div class="text-left">
                <span class="flex items-center justify-start gap-4">
                    <h2 class="text-3xl font-semibold">
                        Links 
                    </h2>
                    <i class="fa fa-link text-white text-sm"></i>
                </span>
                <div class="p-4">
                    <span class="flex items-center gap-4">
                        <i class="fa fab fa-github text-slate-900 text-4xl"></i>
                        <a href="https://github.com/saman-zand-h/pezeshkino" class="hover:underline underline-offset-2">
                            https://github.com/saman-zand-h/pezeshkino
                        </a>
                    </span>
                </div>
            </div>
        </main>
        <Footer />
    </div>
</template>


<script lang="ts">
    import 'swiper/css';
    import 'swiper/css/navigation';
    import 'swiper/css/pagination';
    import { defineComponent } from 'vue';
    import { mapState, mapActions } from 'vuex';
    import projectsInterface from '@/store/types/projects';
    import Footer from '@/components/Footer.vue';
    import HomeNavbar from '@/components/HomeNavbar.vue';
    import { Swiper, SwiperSlide } from 'swiper/vue'
    import { EffectFade, Navigation, Pagination } from 'swiper/modules';

    export default defineComponent({
        name: 'ProjectView',
        components: {
            HomeNavbar,
            Swiper,
            SwiperSlide,
            Footer
        },
        computed: {
            ...mapState(["projects"]),
            project(): projectsInterface {
                const slug = this.$route.params["slug"]
                return this.projects.filter((v: projectsInterface) => v.slug === slug)[0]
            }
        },
        methods: {
            ...mapActions(["update_projects"])
        },
        async beforeMount() {
            await this.update_projects()
            document.title = `Project ${this.project.name}`
        },
        setup() {
            return {
                modules: [Navigation, Pagination, EffectFade]
            }
        }
    })
</script>