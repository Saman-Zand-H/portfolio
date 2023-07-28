<template>
    <div :class="[isActive ? 'w-full md:w-1/3 lg: 1/4' : 'w-0', 'absolute h-full z-50 right-0 inset-y-0 bg-zinc-900 transition-all duration-300 overflow-hidden']">
        <button type="button" @click.prevent="$emit('toggle-sidebar')" class="">
            Close
        </button>
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
        emits: ["toggle-sidebar"]
    })

    export default class HomeSidebar extends Vue {
        isActive!: Boolean
    }
</script>