<template>
    <div 
        class="rounded-3xl project-card w-1/3 aspect-square flex flex-col justify-center text-center items-center p-5 bg-cover shadow-md"
        :style="backgroundName ? `background-image: url(${require('../assets/'+backgroundName)})` : ''"
    >
        {{ text }}
    </div>
</template>

<script lang="ts">
    import { Options, Vue } from 'vue-class-component';

    @Options({
        props: {
            backgroundName: {
                type: String,
                required: false,
                default: null
            },
            text: {
                type: String,
                required: false,
                default: null
            }
        }
    })

    export default class ProjectPortfolioCard extends Vue {
        backgroundName!: String
        text!: String
    }
</script>