<template>
    <div class="grid grid-cols-1 w-full md:grid-cols-2 gap-2">
        <div class="bg-transparent grid custom-grid-row-6 gap-2">
            <div class="rounded-3xl text-start row-span-4 xl:row-span-3 h-full bg-zinc-800/70 text-5xl font-bold p-6 text-white leading-[2.6rem] md:leading-none">
                Bringing Your Ideas To Life Through a FullStack Development
                <span class="rounded-full bg-violet-500 text-sm p-2 ms-3">Hire me</span>
            </div>
            <div class="grid grid-cols-3 gap-4 row-span-2 xl:row-span-3 h-full w-full bg-transparent text-center">
                <div class="bg-green-500 rounded-3xl flex flex-col gap-2 items-center justify-center text-white">
                    <span class="text-3xl font-bold">1</span>
                    <small clas="text-xs">Year of Experince in Vue.js</small>
                </div>
                <div class="bg-amber-300 rounded-3xl flex items-center justify-center text-black flex-col gap-2">
                    <span class="text-3xl font-bold">4+</span>
                    <small clas="text-xs">Years of Experince in python</small>
                </div>
                <div class="bg-rose-400 rounded-3xl flex items-center justify-center text-white flex-col gap-2">
                    <span class="text-3xl font-bold">10+</span>
                    <small clas="text-xs">Handled Projects</small>
                </div>
            </div>
        </div>
        <div class="w-full grid custom-grid-row-6 gap-16 xl:gap-1 bg-transparent items-start">
            <div class="rounded-3xl row-span-1 bg-zinc-800/70 text-xl flex justify-between font-semibold p-5 text-white">
                <span class="font-sans">SamanZND</span>
                <span class="hover:cursor-pointer hover:text-zinc-300 transition-colors duration-300"><i class="fa fa-bars"></i></span>
            </div>
            <div class="gap-2 grid grid-cols-1 md:grid-cols-2 row-span-5 bg-transparent text-center">
                <div class="h-full">
                    <img src="../assets/saman.jpg" class="rounded-3xl object-fill">
                </div>
                <div class="rounded-3xl bg-transparent grid gap-3 custom-grid-row-5">
                    <div class="row-span-1 bg-zinc-800/70 rounded-3xl text-white flex justify-between items-center px-6">
                        <span>Name :</span>
                        <b class="font-bold">Saman Zand</b>
                    </div>
                    <div class="row-span-3 flex-col gap-3 bg-zinc-800/70 rounded-3xl text-white flex justify-start items-center p-4">
                        <div class="flex justify-between w-full px-2">
                            <span>Based in :</span>
                            <b>Mashhad</b>
                        </div>
                        <img src="../assets/mashhadMap.png" class="rounded-3xl w-full aspect-auto">
                    </div>
                    <div class="row-span-1 bg-zinc-800/70 rounded-3xl text-white flex justify-between items-center px-6">
                        <span><i class="fa fab rounded-[100%] py-1 px-2 lg:py-2 lg:px-3 fa-github text-2xl bg-slate-800"></i></span>
                        <span><i class="fa fab rounded-[100%] py-1 px-2 lg:py-2 lg:px-3 fa-linkedin text-2xl bg-blue-900"></i></span>
                        <span><i class="fa fab rounded-[100%] py-1 px-2 lg:py-2 lg:px-3 fa-telegram text-2xl bg-cyan-700"></i></span>
                        <span><i class="fa fab rounded-[100%] py-1 px-2 lg:py-2 lg:px-3 fa-instagram text-2xl bg-gradient-to-br from-orange-400 to-purple-700"></i></span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="grid grid-cols-1 w-full md:grid-cols-5 gap-3 mt-3">
        <div class="rounded-3xl col-span-3 bg-zinc-800/70 row text-white p-6 text-2xl text-left">
            <div class="flex justify-between">
                <b>Projects Portfolio</b>
                <span class="text-zinc-400 hover:cursor-pointer hover:text-zinc-400/80">
                    View All
                </span>
            </div>
            <div class="mt-2 flex flex-row gap-2">
                <ProjectPortfolioCard backgroundName="logo.png" />
                <ProjectPortfolioCard backgroundName="logo.png" />
                <ProjectPortfolioCard backgroundName="logo.png" />
            </div>
        </div>
        <div class="rounded-3xl col-span-2 bg-zinc-800/70 text-white p-6 text-xl text-left">
            <div class="flex justify-between">
                <b>About</b>
                <span class="text-zinc-400">Resume</span>
            </div>
            <div class="mt-2 text-sm text-zinc-300">
                <small>Hi, I'm an accomplished Full-Stack Developer with 4 years of hands-on experience in Python. During this time, I've successfully delivered a range of projects, from web applications to backend systems, which have deepened my expertise and proficiency in Python development. Additionally, I have 1 year of proven experience in Vue.js, creating engaging user interfaces. My dedication to innovation and problem-solving drives me to stay updated with the latest technologies. Eager to contribute my skills to impactful projects and collaborate with dynamic teams. Samples available upon request. Let's achieve excellence together!</small>
            </div>
        </div>
    </div>
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

<script lang="ts">
import { Vue, Options } from 'vue-class-component';
import ProjectPortfolioCard from './ProjectPortfolioCard.vue';

@Options({
    components: {
        ProjectPortfolioCard
    }
})

export default class HomeBlocks extends Vue { }
</script>
