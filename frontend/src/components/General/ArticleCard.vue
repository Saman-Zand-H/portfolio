<template>
    <router-link 
        :to="{ name: 'article', params: {slug: isUndefined(article?.slug) ? 'unknown' : article?.slug}}" 
        class="h-fit w-fit md:w-2/3 mx-auto flex transition-colors gap-3 duration-200 p-2 sm:p-5 bg-contain rounded-3xl text-white"
        >
        <div class="w-fit flex flex-col items-center border-e-2 pe-3 h-fit">
            <span class="text-xs sm:text-sm">{{ jmoment(article?.updated_at).format('jMMMM') }}</span>
            <span class="text-base sm:text-2xl font-semibold">{{ jmoment(article?.updated_at).format('jD') }}</span>
            <span class="text-xs sm:text-sm">{{ jmoment(article?.updated_at).format('jYYYY') }}</span>
        </div>
        <div class="flex flex-wrap flex-col h-fit justify-center gap-1">
            <span class="font-semibold text-base sm:text-2xl hover:text-emerald-500 transition-colors duration-300">{{ article?.title }}</span>
            <span class="text-xs sm:text-sm text-gray-400">{{ article?.subtitle }}</span>
        </div>
    </router-link>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import isUndefined from 'lodash/isUndefined';
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
                jmoment,
                isUndefined
            }
        }
    })
</script>