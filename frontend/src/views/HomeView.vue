<template>
    <div class="w-full h-full relative bg-zinc-950">
        <HomeBlocks />
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import HomeBlocks from '@/components/HomeBlocks.vue'; // @ is an alias to /src

@Options({
    components: {
        HomeBlocks,
    },
})
export default class HomeView extends Vue { }
</script>
