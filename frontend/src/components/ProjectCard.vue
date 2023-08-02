<template>
    <div class="w-full animate__animated animate__fadeInUp flex flex-col gap-5 sm:w-1/2 md:w-1/3 lg:w-1/4 bg-zinc-800 text-white px-4 py-6 rounded-3xl">
        <div class="w-2/3 rounded-3xl overflow-hidden self-center shadow-lg">
            <img 
                    class="w-full aspect-square" 
                    :src="!isEmpty(project.images) ? project.images[0].image : require('../assets/logo.png')"
                >
        </div>
        <div class="flex flex-col gap-2">
            <span class="font-bold text-3xl">{{ project.name }}</span>
            <span class="text-xs">{{ jmoment(project.started_at).format("jYYYY-jMM-jDD") }}</span>
        </div>
        <div class="px-3" style="direction: rtl">
            <small class="text-xs">
                {{ project.explanations.split(" ").slice(0, 15).join(" ") }}...
            </small>
        </div>
        <div class="flex gap-2 px-5 flex-wrap">
            <a v-for="tech in project.technologies.slice(0, 4)" :href="tech.url" class="rounded-lg p-1 bg-zinc-100/10 hover:bg-zinc-10/5">
                <img :src="tech.icon" :alt="tech.name" :aria-label="tech.name" width="30" height="40" class="hover:opacity-80">
            </a>...
        </div>
        <div class="flex justify-end">
            <router-link :to="{ name: 'project', params: {slug: project.slug} }" class="p-4 rounded-2xl bg-indigo-600">Read More</router-link>
        </div>
    </div>
</template>

<script lang="ts">
    // @ts-ignore
    import isEmpty from 'lodash/isEmpty';
    import { defineComponent } from 'vue';
    import projectsInterface from '@/store/types/projects';
    // @ts-ignore
    import jmoment from 'moment-jalaali';
    // @ts-ignore
    import moment from 'moment';
    // @ts-ignore
    import fa from 'moment/locale/fa';

    export default defineComponent({ 
        name: 'ProjectCard',
        props: {
            project: {
                type: Object as ()=> projectsInterface,
                required: true
            } 
        },
        setup() {
            moment.updateLocale("fa", fa)
            jmoment.loadPersian()
            return {
                isEmpty,
                jmoment
            }
        },
    })
</script>
