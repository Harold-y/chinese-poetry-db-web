<template>
    <div style="max-width:70%; padding: 1rem; margin: auto; margin-top: 8%;">
        <n-space justify="center">
            <n-select v-model:value="query_option" :options="options" style="width: 110px;"/>
            <n-auto-complete
                    v-model:value="query_text"
                    placeholder="信息"
                    clearable
            />
            <n-button @click="search">查询</n-button>
        </n-space> 
    </div>
    <div style="max-width:70%; padding: 1rem; margin: auto; margin-top: 8%; margin-top: 4rem; max-width: 500px;">
        <img
            src="DSC07440.jpg"
            style="max-width: 100%; height: auto; width: auto\9;"
        />
    </div>
        
</template>
    
<script>
    import { defineComponent} from 'vue'
    import { NAutoComplete, NButton, NGrid, NGi, NSelect, NSpace, useMessage  } from 'naive-ui';
    import router from "../router/index.js";
    
    export default defineComponent({
        components: {
            NAutoComplete, NButton, NGrid, NGi, NSelect, NSpace
        },
        methods: {
            search: function() {
                if (this.query_text === null || this.query_text === '')
                {
                    this.createMessage()
                }else {
                    router.push('/search_poem_list/' + this.query_option + '/' + this.query_text)
                }
                
            },
            
        }, mounted() {

        }, data () {
            return {
            query_option: 'title',
            query_text: '',
            options: [
                {
                    label: '标题',
                    value: 'title',
                },
                {
                    label: '正文',
                    value: 'para'
                },
                {
                    label: '词牌/韵律',
                    value: 'rhy'
                },
                {
                    label: '作者',
                    value: 'author'
                },
            ]
            }
        }, setup() {
            const message = useMessage()
            return {
                createMessage () {
                message.info(
                    "查询内容不能为空",
                    { duration: 4000 }
                )
            }
            };
        }, props: {
        
        }
    })

</script>

<style>

</style>