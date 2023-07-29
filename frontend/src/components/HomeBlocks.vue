<template>
    <HomeSidebar :isActive="isActive" @toggle-sidebar="isActive = !isActive" />
    <div class="fixed w-full h-full bg-zinc-700/50 z-20" v-if="isActive"></div>
    <main class="p-5">
        <div class="grid grid-cols-1 w-full md:grid-cols-2 gap-2">
            <div class="bg-transparent grid custom-grid-row-6 gap-2">
                <div class="rounded-3xl text-start row-span-3 xl:row-span-3 h-full bg-zinc-800/70 font-bold p-6 text-white leading-[2.6rem] md:leading-none" style="font-size: 3.6vw">
                    Bringing Your Ideas To Life Through a FullStack Development
                    <span class="rounded-full bg-violet-500 text-sm py-2 px-3 ms-3">
                        Hire me
                        
                    </span>
                </div>
                <div class="grid grid-cols-3 gap-4 row-span-3 xl:row-span-3 h-full w-full bg-transparent text-center">
                    <div class="bg-green-500 rounded-3xl flex flex-col gap-2 items-center justify-center text-white">
                        <span class="font-bold" style="font-size: 2.7vw">1</span>
                        <small style="font-size: .92vw">Year of Experince in Vue.js</small>
                    </div>
                    <div class="bg-amber-300 rounded-3xl flex items-center justify-center text-black flex-col gap-2">
                        <span class="font-bold" style="font-size: 2.7vw">4+</span>
                        <small style="font-size: .92vw">Years of Experince in python</small>
                    </div>
                    <div class="bg-rose-400 rounded-3xl flex items-center justify-center text-white flex-col gap-2">
                        <span class="font-bold" style="font-size: 2.7vw">10+</span>
                        <small style="font-size: .92vw">Handled Projects</small>
                    </div>
                </div>
            </div>
            <div class="w-full grid custom-grid-row-6 gap-16 xl:gap-1 bg-transparent items-start">
                <div class="rounded-3xl row-span-1 bg-zinc-800/70 flex justify-between font-semibold p-5 text-white" style="font-size: 1.7vw">
                    <span class="font-sans">SamanZND</span>
                    <button type="button" id="sidebarBurger" @click.prevent="isActive = !isActive" class="hover:cursor-pointer hover:text-zinc-300 transition-colors duration-300"><i class="fa fa-bars"></i></button>
                </div>
                <div class="gap-2 grid grid-cols-1 md:grid-cols-2 row-span-5 bg-transparent text-center">
                    <div class="h-full">
                        <img :src="cv.image" class="rounded-3xl object-fill">
                    </div>
                    <div class="rounded-3xl bg-transparent grid gap-3 custom-grid-row-5">
                        <div class="row-span-1 bg-zinc-800/70 rounded-3xl text-white flex justify-between items-center px-6" style="font-size: 1.3vw">
                            <span>Name :</span>
                            <b class="font-bold">Saman Zand</b>
                        </div>
                        <div class="row-span-3 flex-col gap-3 bg-zinc-800/70 rounded-3xl text-white flex justify-start items-center p-4" style="font-size: 1.2vw">
                            <div class="flex justify-between w-full px-2">
                                <span>Based in :</span>
                                <b>{{ cv.location }}</b>
                            </div>
                            <img src="../assets/mashhadMap.png" class="rounded-3xl w-full aspect-auto">
                        </div>
                        <div class="row-span-1 bg-zinc-800/70 rounded-3xl text-white flex justify-between items-center px-6">
                            <a href="https://github.com/saman-zand-h" class="inline-block"><i class="fa fab rounded-[100%] py-1 px-2 lg:py-2 lg:px-2 fa-github bg-slate-800" style="font-size: 2vw"></i></a>
                            <a href="https://linkedin.com/saman-zand-h" class="inline-block"><i class="fa fab rounded-[100%] py-1 px-2 lg:py-2 lg:px-2 fa-linkedin bg-blue-900" style="font-size: 2vw"></i></a>
                            <a href="https://telegram.me/robsaman" class="inline-block"><i class="fa fab rounded-[100%] py-1 px-2 lg:py-2 lg:px-2 fa-telegram bg-cyan-700" style="font-size: 2vw"></i></a>
                            <a href="https://instagram.com/t.n.saman" class="inline-block"><i class="fa fab rounded-[100%] py-1 px-2 lg:py-2 lg:px-2 fa-instagram bg-gradient-to-br from-orange-400 to-purple-700" style="font-size: 2vw"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="grid grid-cols-1 w-full md:grid-cols-5 gap-3 mt-3">
            <div class="rounded-3xl col-span-3 bg-zinc-800/70 row text-white p-6 text-left" style="font-size: 1.8vw">
                <div class="flex justify-between">
                    <b>Projects Portfolio</b>
                    <span class="text-zinc-400 transition-colors duration-200 hover:cursor-pointer hover:text-zinc-400/80">
                        View All
                    </span>
                </div>
                <div class="mt-2 flex flex-row gap-2">
                    <ProjectPortfolioCard v-if="!isEmpty(projects)" v-for="project in projects" :key="project.slug" :backgroundName="project.images[0].image" />
                </div>
            </div>
            <div class="rounded-3xl col-span-2 bg-zinc-800/70 text-white p-6 text-xl text-left">
                <div class="flex justify-between">
                    <b>About</b>
                    <span class="text-zinc-400">Resume</span>
                </div>
                <div class="mt-2 text-sm text-zinc-300">
                    <small>{{ cv.about }}</small>
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@700&display=swap');
    .custom-grid-row-6 {
        grid-template-rows: repeat(6, minmax(0, .2fr));
    }
    .custom-grid-row-5 {
        grid-template-rows: repeat(5, minmax(0, .2fr));
    }
    div {
        font-family: 'Space Mono', monospace
    }
</style>

<style>
    body {
        display: relative
    }
</style>

<script lang="ts">
import ProjectPortfolioCard from './ProjectPortfolioCard.vue';
import { cvInterface, projectsInterface } from '@/store/index'
import { Vue, Options } from 'vue-class-component';
import HomeSidebar from './HomeSidebar.vue';
import { mapState, mapActions } from 'vuex';
import isEmpty from 'lodash/isEmpty'

@Options({
    components: {
        ProjectPortfolioCard,
        HomeSidebar
    },
    computed: {
        ...mapState(["cv", "projects"])
    },
    methods: {
        ...mapActions(["update_cv", "update_projects"])
    },
    data() {
        return {
            isActive: false
        }
    },
    setup() {
        return {
            isEmpty
        }
    },
    async beforeMount() {
        await this.update_cv()
        await this.update_projects()
    }
})

export default class HomeBlocks extends Vue {
    cv!: cvInterface
    projects!: Array<projectsInterface>
    isActive!: boolean
    isEmpty!: isEmpty
}
</script>
