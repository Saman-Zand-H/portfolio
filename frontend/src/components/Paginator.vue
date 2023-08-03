<template>
    <Pagination @update:model-value="$emit('page-changed', $event)" v-model="page" :total-pages="pages" :slice-length="5" />
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import { Pagination } from 'flowbite-vue';
    import { toNumber } from 'lodash';

    export default defineComponent({
        name: 'Paginator',
        data() {
            const page = this.$route.query.page;
            return {
                page: page ? toNumber(page) : 1
            }
        },
        components: {
            Pagination
        },
        emits: ["page-changed"],
        props: {
            pages: Number
        }
    })
</script>