<template>
    <div class="bg-zinc-950 max-h-full min-h-screen w-full p-5">
        <HomeNavbar />
        <main class="my-3" v-for="project in projects">
            <ProjectCard :project="project" />
        </main>
        <Footer />
    </div>
</template>

<script lang="ts">
    import { mapActions, mapState } from 'vuex';
    import { defineComponent } from 'vue';
    import Footer from '@/components/General/Footer.vue';
    import HomeNavbar from '@/components/General/Navbar.vue';
    import ProjectCard from '@/components/General/ProjectCard.vue';

    export default defineComponent({
        name: "ProjectsListView",
        components: {
            HomeNavbar,
            ProjectCard,
            Footer
        },
        methods: {
            ...mapActions(["update_projects"])
        },
        computed: {
            ...mapState(["projects"])
        },
        async beforeMount() {
            await this.update_projects()
        }
    })
</script>