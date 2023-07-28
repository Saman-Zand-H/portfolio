<template>
    <div 
        :class="['rounded-3xl bg-blend-darken project-card w-1/3',
                 'aspect-square flex scale-75 hover:shadow-lg hover:scale-[85%] hover:cursor-pointer',
                 'duration-300 transition-all flex-col justify-center',
                 'text-center items-center p-5 bg-contain shadow-md']"
        :style="backgroundName ? `background-image: url(${require('../assets/'+backgroundName)})` : ''"
    >
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
            }
        }
    })

    export default class ProjectPortfolioCard extends Vue {
        backgroundName!: String
        text!: String
    }
</script>