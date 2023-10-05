<template>
    <n-grid
        :cols="5"
        :collapsed="gridCollapsed"
        :collapsed-rows="gridCollapsedRows"
    >
        <n-gi
        v-for="i in gridItemCount"
        :key="i"
        :class="i % 2 ? 'green' : 'light-green'"
        >
        {{ i }}
        </n-gi>
        <n-gi v-if="showSuffix" suffix class="suffix" #="{ overflow }">
        {{ overflow ? '存在溢出' : '不存在溢出' }}
        </n-gi>
    </n-grid>
</template>
    
<script>
    import { defineComponent} from 'vue'
    import { NButton, NGrid, NGi, NSpace } from 'naive-ui';
    export default defineComponent({
        components: {
            NButton, NGrid, NGi, NSpace
        },
        methods: {

        }, mounted() {

        }, data () {
            return {
                gridItemCount: 5,
            
            }
        }, setup() {
            return {
                
            };
        }, props: {
        
        }
    })

</script>

<style>

</style>