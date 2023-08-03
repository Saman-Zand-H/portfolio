<template>
    <div class="flex flex-col gap-3">
        <div class="flex gap-10 text-gray-400 justify-center">
            <a href="https://github.com/saman-zand-h/" class="flex text-5xl gap-5 hover:text-gray-400/80 transition-colors duration-200">
                <i class="fa fab fa-github"></i>
            </a>
            <a href="https://linkedin.com/in/saman-zand-h/" class="flex text-5xl gap-5 hover:text-gray-400/80 transition-colors duration-200">
                <i class="fa fab fa-linkedin"></i>
            </a>
            <a href="https://telegram.me/robsaman/" class="flex text-5xl gap-5 hover:text-gray-400/80 transition-colors duration-200">
                <i class="fa fab fa-telegram"></i>
            </a>
        </div>
        <span class="font-semibold">
            2023 &copy; Saman Zand Haghighi
        </span>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        'name': 'Footer'
    })
</script>