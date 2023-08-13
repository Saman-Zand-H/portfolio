<template>
    <HomeSidebar :isActive="isActive" @toggle-sidebar="isActive = !isActive" />
    <div class="fixed w-full min-h-screen max-h-full bg-zinc-700/50 z-20" v-if="isActive"></div>
    <main class="p-5">
        <div class="flex flex-col gap-3 lg:grid grid-cols-1 w-full lg:grid-cols-2 lg:gap-2">
            <div class="rounded-3xl lg:hidden animate__animated animate__fadeInUp w-full text-xl row-span-1 bg-zinc-800/70 flex justify-between font-semibold p-5 text-white">
                <router-link :to="{ name: 'home' }" class="font-sans text-white hover:text-zinc-200">SamanZND</router-link>
                <button type="button" title="Toggle Sidebar" @click.prevent="isActive = !isActive" class="hover:cursor-pointer hover:text-zinc-300 transition-colors duration-300"><i class="fa fa-bars"></i></button>
            </div>
            <div class="bg-transparent flex flex-col gap-3 lg:grid grid-rows-2 xl:grid-rows-6 lg:gap-2">
                <!-- The big text box at the top -->
                <div class="rounded-3xl animate__animated animate__fadeInUp flex flex-wrap gap-x-3 items-bae text-start row-span-1 xl:row-span-3 h-full bg-zinc-800/70 font-bold p-6 text-white leading-[2.6rem] lg:leading-none">
                    <span class="text-3xl sm:text-4xl lg:text-5xl" v-for="word in 'Bringing Your Ideas To Life Through a FullStack Development'.split(' ')">
                        {{ word }}
                    </span>
                    <span class="rounded-full mt-2 bg-violet-500 hover:bg-violet-500/80 hover:cursor-pointer transition-colors duration-200 py-1 px-3 ms-2 flex items-center">
                        Hire me
                        &#128075;
                    </span>
                </div>
                <!-- The vibrant boxes -->
                <div class="grid grid-cols-3 gap-4 row-span-1 xl:row-span-3 h-full w-full bg-transparent text-center">
                    <div class="bg-green-500 rounded-3xl animate__animated animate__fadeInUp p-6 flex flex-col gap-2 items-center justify-center text-white">
                        <span class="font-bold text-2xl">1</span>
                        <small class="text-xs">Year of Experince in Vue.js</small>
                    </div>
                    <div class="bg-amber-300 rounded-3xl animate__animated animate__fadeInUp p-6 flex items-center justify-center text-black flex-col gap-2">
                        <span class="font-bold text-2xl">+4</span>
                        <small class="text-xs">Years of Experince in python</small>
                    </div>
                    <div class="bg-rose-400 rounded-3xl animate__animated animate__fadeInUp p-6 flex items-center justify-center text-white flex-col gap-2">
                        <span class="font-bold text-2xl">+10</span>
                        <small class="text-xs">Handled Projects</small>
                    </div>
                </div>
            </div>
            <div class="w-full flex flex-col gap-2 lg:grid sm:grid-rows-6 bg-transparent items-start">
                <div class="rounded-3xl hidden lg:flex animate__animated animate__fadeInUp w-full text-xl row-span-1 bg-zinc-800/70 justify-between font-semibold p-5 text-white">
                    <router-link :to="{ name: 'home' }" class="font-sans text-white text-lg md:text-2xl hover:text-zinc-200">SamanZND</router-link>
                    <button type="button" id="sidebarBurger" @click.prevent="isActive = !isActive" title="Toggle Sidebar" class="hover:cursor-pointer hover:text-zinc-300 transition-colors duration-300"><i class="fa fa-bars"></i></button>
                </div>
                <div class="flex lg:flex-row flex-col gap-3 w-full h-full row-span-5 bg-transparent text-center">
                    <div class="h-auto w-full animate__animated animate__fadeInUp lg:w-1/2 rounded-3xl overflow-hidden bg-zinc-800 lg:bg-cover" :style="`background-image: url(${cv.image})`">
                        <img class="lg:hidden w-full h-fit" alt="SamanZnd" :src="cv.image">
                    </div>
                    <div class="rounded-3xl w-full lg:w-1/2 bg-transparent grid grid-cols-1 gap-3">
                        <div class="row-span-1 animate__animated animate__fadeInUp bg-zinc-800/70 rounded-3xl text-white flex justify-between items-center flex-wrap gap-5 px-6 py-6 lg:py-0">
                            <span class="text-base md:text-xl">Name :</span>
                            <b class="text-base md:text-xl">Saman Zand</b>
                        </div>
                        <div class="row-span-3 animate__animated animate__fadeInUp flex-col gap-3 bg-zinc-800/70 rounded-3xl text-white flex justify-start items-center p-5">
                            <div class="flex justify-between w-full p-2 flex-wrap gap-5">
                                <span class="text-lg md:text-xl">Based in :</span>
                                <b class="text-base md:text-xl">{{ cv.location }}</b>
                            </div>
                            <div class="rounded-3xl overflow-hidden w-full h-full bg-cover" :style="`background-image: url(${require('../assets/mashhadMap.png')})`">
                                <img class="w-full h-full lg:hidden" alt="Mashhad Map" src="../assets/mashhadMap.png">
                            </div>
                        </div>
                        <div class="row-span-1 animate__animated animate__fadeInUp bg-zinc-800/70 rounded-3xl text-white flex justify-between gap-2 items-center flex-wrap px-6 py-6 lg:py-0">
                            <a href="https://github.com/saman-zand-h" aria-label="GitHub" class="inline-block"><i class="fa fab rounded-[100%] hover:opacity-90 p-3 lg:p-2 fa-github bg-slate-800 text-3xl lg:text-2xl"></i></a>
                            <a href="https://linkedin.com/saman-zand-h" aria-label="LinkedIn" class="inline-block"><i class="fa fab rounded-[100%] hover:opacity-90 p-3 lg:p-2 fa-linkedin bg-blue-900 text-3xl lg:text-2xl"></i></a>
                            <a href="https://telegram.me/robsaman" aria-label="Telegram" class="inline-block"><i class="fa fab rounded-[100%] hover:opacity-90 p-3 lg:p-2 fa-telegram bg-cyan-700 text-3xl lg:text-2xl"></i></a>
                            <a href="https://instagram.com/t.n.saman" aria-label="Instagram" class="inline-block"><i class="fa fab rounded-[100%] hover:opacity-90 p-3 lg:p-2 fa-instagram bg-gradient-to-br from-orange-400 to-purple-700 text-3xl lg:text-2xl"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="rounded-3xl bg-zinc-800 mt-3 animate__animated animate__fadeInUp p-6 text-white text-left">
            <h2 class="font-semibold text-lg md:text-2xl">My Skills:</h2>
            <div class="my-3">
                <swiper
                    :space-between="50"
                    :slides-per-view="1"
                    :breakpoints="swiperBreakpoints"
                    :loop="true"
                    :centeredSlides="true"
                    :autoplay="{
                        delay: 2500,
                        disableOnInteraction: false,
                    }"
                    :navigation="true"
                    :modules="modules"
                    class="mt-5"
                >
                    <swiper-slide class="p-6" v-for="tech in technologies">
                        <a :href="tech.url" :aria-label="tech.name" class="rounded-2xl flex items-center justify-center h-fit p-1">
                            <img class="hover:opacity-80 transition-opacity duration-300" width="60" height="70" :src="tech.icon" :alt="tech.name">
                        </a>
                    </swiper-slide>
                </swiper>
            </div>
        </div>
        <div class="rounded-3xl w-full bg-zinc-800 mt-3 animate__animated animate__fadeInUp p-6 text-white text-left">
            <div class="flex justify-between">
                <span>
                    <h2 class="font-semibold text-lg md:text-2xl">My Blog:</h2>                                                                                                                                                                                                                                                                                                                                                                                                    
                </span>
                <router-link :to="{ name: 'blog' }" aria-label="Blog">
                    <h2 class="font-semibold text-base md:text-xl text-zinc-500 hover:text-zinc-500/80 hover:cursor-pointer">View All</h2>
                </router-link>
            </div>
            <div class="w-full p-5">
                <BlogPortfolioCard v-for="article in articles" :article="article" />
            </div>
        </div>
        <div class="lg:grid w-full lg:grid-cols-5 flex flex-col gap-3 mt-3">
            <div class="rounded-3xl col-span-3 animate__animated animate__fadeInUp bg-zinc-800/70 row text-white p-6 text-left">
                <div class="flex justify-between">
                    <b class="text-lg md:text-2xl">Projects</b>
                    <router-link :to="{ name: 'projects' }" class="text-zinc-400 text-base md:text-xl transition-colors duration-200 hover:text-zinc-400/80">
                        View All
                    </router-link>
                </div>
                <div class="mt-2 flex flex-row gap-2 overflow-x-auto">
                    <router-link :to="{ name: 'project', params: { slug: project.slug } }" :aria-label="project.slug" class="h-full w-full" v-for="project in projects" :key="project.slug">
                        <ProjectPortfolioCard 
                                v-if="!isEmpty(project.images)"
                                :backgroundUrl="project.images[0]?.image" 
                            />
                    </router-link>
                </div>
            </div>
            <div class="rounded-3xl w-full col-span-2 animate__animated animate__fadeInUp bg-zinc-800/70 text-white p-6 text-xl text-left">
                <div class="flex justify-between">
                    <b class="text-lg md:text-2xl">About</b>
                    <Dropdown>
                        <template #trigger="{ toggle }">
                            <button class="text-zinc-400 text-base md:text-xl" @click="toggle">
                                Resume
                            </button>
                        </template>
                        <ul class="text-xs p-2">
                            <li class="w-full">
                                <a :href="require('@/assets/en-cv.pdf')" download="saman-zand-h-EN.pdf">
                                    EN
                                </a>
                            </li>
                            <li class="w-full">
                                <a :href="require('@/assets/fa-cv.pdf')" download="saman-zand-h-FA.pdf">
                                    FA
                                </a>
                            </li>
                        </ul>
                    </Dropdown>
                </div>
                <div class="mt-2 text-sm text-zinc-300">
                    <small>{{ cv.about }}</small>
                </div>
            </div>
        </div>
    </main>
</template>

<style>
    body {
        display: relative
    }
</style>

<script lang="ts">
import ProjectPortfolioCard from './ProjectPortfolioCard.vue';
import BlogPortfolioCard from './BlogPortfolioCard.vue';
import { Autoplay, Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import HomeSidebar from './HomeSidebar.vue';
import { mapState, mapActions } from 'vuex';
import { Dropdown } from 'flowbite-vue';
import { defineComponent } from 'vue';
import isEmpty from 'lodash/isEmpty';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css';


export default defineComponent({
    name: 'HomeBlocks',
    components: {
        ProjectPortfolioCard,
        HomeSidebar,
        Swiper,
        SwiperSlide,
        BlogPortfolioCard,
        Dropdown
    },
    computed: {
        ...mapState(
            [
                "cv", 
                "projects", 
                "technologies", 
                "articles"
            ]
        )
    },
    methods: {
        ...mapActions(
            [
                "update_cv", 
                "update_projects", 
                "update_technologies", 
                "get_preview"
            ]
        )
    },
    data() {
        return {
            isActive: false
        }
    },
    setup() {
        return {
            isEmpty,
            modules: [Autoplay, Navigation],
            swiperBreakpoints: {
                470: {
                    slidesPerView: 2,
                    spaceBetween: 30
                },
                540: {
                    slidesPerView: 4
                },
                800: {
                    slidesPerView: 5
                },
                1025: {
                    slidesPerView: 8
                }
            }
        }
    },
    async beforeMount() {
        await this.update_cv()
        await this.update_projects()
        await this.update_technologies()
        await this.get_preview()
    }
})
</script>
