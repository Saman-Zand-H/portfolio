<template>
    <div class="bg-zinc-950 text-white max-h-full min-h-screen w-full p-5">
        
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import { mapState, mapActions } from 'vuex';

    export default defineComponent({
        name: 'ArticlesListView',
        computed: {
            ...mapState(["articles"])
        },
        methods: {
            ...mapActions(["update_articles"])
        },
        async beforeMount() {
            await this.update_articles(true)
        }
    })
</script>