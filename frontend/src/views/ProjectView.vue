<template>
    <div class="min-h-screen max-h-full bg-zinc-950 p-5">
        <HomeNavbar />
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import HomeNavbar from '@/components/HomeNavbar.vue';

    export default defineComponent({
        name: 'ProjectView',
        components: {
            HomeNavbar
        }
    })
</script>