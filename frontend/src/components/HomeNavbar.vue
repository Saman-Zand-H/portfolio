<template>
    <div class="bg-zinc-800 rounded-3xl w-full text-white flex flex-col shadow-lg">
        <nav class="h-14 flex items-center justify-between px-8 text-xl font-bold">
            <span>SamanZND</span>
            <button type="button" @click.prevent="isActive = !isActive"><i class="fa fa-bars text-2xl"></i></button>
        </nav>
        <ul :class="[isActive ? 'max-h-screen' : 'max-h-0', 'w-full transition-[max-height] overflow-hidden duration-500 flex flex-col']">
            <router-link :to="{ name: 'home' }" class="border-t hover:cursor-pointer hover:bg-zinc-950/80 border-zinc-950 py-4">
                Home
            </router-link>
            <router-link :to="{ name: 'projects' }" class="border-t hover:cursor-pointer hover:bg-zinc-950/80 border-zinc-950 py-4">
                Projects
            </router-link>
        </ul>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'HomeNavbar',
        data() {
            return {
                isActive: false
            }
        },
    })
</script>