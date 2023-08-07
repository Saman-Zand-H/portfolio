<template>
    <div id="sidebarContainer" :class="[isActive ? 'w-full md:w-1/3 lg: 1/4' : 'w-0', 'fixed min-h-screen max-h-full z-50 right-0 py-7 inset-y-0 bg-zinc-900 transition-all duration-300 overflow-hidden']">
        <div class="my-6">
            <router-link :to="{ name: 'home' }" class="text-white font-mono text-3xl">
                SamanZND
            </router-link>
        </div>
        <button type="button" @click.prevent="$emit('toggle-sidebar')" class="text-white hover:bg-zinc-800/30 border-y border-white py-4 w-full">
            Close
        </button>
        <router-link :to="{ name: 'blog' }" class="text-white block hover:bg-zinc-800/30 border-y border-white py-4 w-full">
            Blog
        </router-link>
        <router-link :to="{ name: 'projects' }" class="text-white block hover:bg-zinc-800/30 border-y border-white py-4 w-full">
            Projects
        </router-link>
    </div>
</template>

<script lang="ts">
    import { Options, Vue } from 'vue-class-component'

    @Options({
        props: {
            isActive: {
                type: Boolean,
                required: true
            }
        },
        emits: ["toggle-sidebar"],
        mounted() {
            window.onclick = e => {
                if (this.isActive && e.target instanceof Element) {
                    const sidebar = document.getElementById("sidebarContainer");
                    const sidebarBurger = document.getElementById("sidebarBurger")
                    if (sidebarBurger?.contains(e.target)) return;
                    if (!sidebar?.contains(e.target)) this.$emit("toggle-sidebar");
                }
            }
        }
    })

    export default class HomeSidebar extends Vue {
        isActive!: Boolean
    }
</script>