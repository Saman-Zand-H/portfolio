<template>
    <ul v-if="!isEmpty(toc)" class="flex flex-col gap-2 p-8 text-center xl:text-start w-full bg-zinc-800/40 xl:bg-transparent xl:p-0 rounded-3xl">
        <li class="text-xl font-semibold flex items-center justify-center xl:justify-start gap-1">
            <svg class="w-6 h-6 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"></path></svg>
            <span>Table of contents</span>
        </li>
        <li class="px-9">
            <Content
                    v-for="[k, v] of Object.entries(toc)" 
                    :key="k"
                    :contentKey="String(k)" 
                    :value="v" 
                />
        </li>
    </ul>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import Content from '@/components/Content.vue'
    import { isEmpty } from 'lodash';

    export default defineComponent({
        name: 'TableOfContents',
        props: {
            toc: {
                type: Object
            }
        },
        setup() {
            return {
                isEmpty
            }
        },
        components: {
            Content
        }
    })
</script>