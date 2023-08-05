<template>
    <li v-if="!isEmpty(value)" class="text-zinc-400">
        <a 
            :href="`#${contentKey.split(',')[1]}`" 
            class="hover:text-zinc-100 transition-colors duration-200"
        >
            {{ contentKey.split(",")[0] }}
        </a>
        <ul :id="contentKey.split(',')[1]" class="py-2 px-4 flex flex-col gap-2">
            <Content 
                    v-for="[k, v] of Object.entries(value)" 
                    :contentKey="String(k)" 
                    :value="v" 
                    :key="k"
                />
        </ul>
    </li>
    <li 
        v-else
        class="text-zinc-400"
    >
        <a :href="`#${contentKey.split(',')[1]}`" class="hover:text-zinc-100 transition-colors duration-200">
            {{ contentKey.split(",")[0] }}
        </a>
    </li>
</template>

<script lang="ts">
    import isEmpty from 'lodash/isEmpty';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'Content',
        props: {
            contentKey: {
                type: String,
                required: true
            },
            value: {
                type: Object,
                required: true
            }
        },
        setup(props) {
            return {
                isEmpty
            }
        }
    })
</script>