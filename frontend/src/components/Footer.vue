<template>
    <footer class="flex flex-col gap-3 animate__animated animate__fadeIn">
        <div class="flex gap-10 justify-center text-gray-400">
            <a href="https://github.com/saman-zand-h/" class="flex text-5xl gap-5 text-gray-400 hover:text-emerald-500 transition-colors duration-200 ease-in">
                <i class="fa fab fa-github"></i>
            </a>
            <a href="https://linkedin.com/in/saman-zand-h/" class="flex text-5xl gap-5 text-gray-400 hover:text-emerald-500 transition-colors duration-200 ease-in">
                <i class="fa fab fa-linkedin"></i>
            </a>
            <a href="https://telegram.me/robsaman/" class="flex text-5xl gap-5 text-gray-400 hover:text-emerald-500 transition-colors duration-200 ease-in">
                <i class="fa fab fa-telegram"></i>
            </a>
        </div>
        <span class="font-semibold">
            2023 - {{ year }} Saman Zand Haghighi
        </span>
    </footer>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import moment from 'moment'

    export default defineComponent({
        'name': 'Footer',
        setup() {
            return {
                year: moment().year()
            }
        }
    })
</script>