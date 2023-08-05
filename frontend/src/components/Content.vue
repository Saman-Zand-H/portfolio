<template>
    <li v-if="!isEmpty(value)">
        <a 
            :href="`#${contentKey.split(',')[1]}`" 
            class="hover:text-zinc-100 text-zinc-400 transition-colors duration-200 toc-heading"
        >
            {{ contentKey.split(",")[0] }}
        </a>
        <ul class="px-3">
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
    >
        <a :href="`#${contentKey.split(',')[1]}`" class="hover:text-zinc-100 text-zinc-400 transition-colors duration-200 toc-heading">
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