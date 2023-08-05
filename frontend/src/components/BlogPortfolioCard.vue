<template>
    <router-link :to="{ name: 'article', params: {slug: article?.slug} }" class="h-fit w-fit md:w-2/3 mx-auto flex transition-colors duration-200 p-5 bg-contain rounded-3xl text-white">
        <div class="w-fit pe-5 flex flex-col items-center border-e-2 h-fit">
            <span class="text-sm">{{ jmoment(article?.updated_at).format('jMMMM') }}</span>
            <span class="text-2xl font-semibold">{{ jmoment(article?.updated_at).format('jD') }}</span>
            <span class="text-sm">{{ jmoment(article?.updated_at).format('jYYYY') }}</span>
        </div>
        <div class="ps-5 flex flex-col h-fit justify-center gap-1">
            <span class="font-semibold text-2xl hover:text-emerald-500 transition-colors duration-300">{{ article?.title }}</span>
            <span class="text-sm text-gray-400">{{ article?.subtitle }}</span>
        </div>
    </router-link>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import { blogInterface } from '@/store/index';
    // @ts-ignore
    import moment from 'moment';
    // @ts-ignore
    import fa from 'moment/locale/fa';
    // @ts-ignore
    import jmoment from 'moment-jalaali';

    export default defineComponent({
        name: 'BlogPortfolioCard',
        props: {
            article: Object as () => blogInterface
        },
        setup() {
            moment.updateLocale('fa', fa);
            jmoment.loadPersian({dialect: 'persian-modern'});
            return {
                jmoment
            }
        }
    })
</script>