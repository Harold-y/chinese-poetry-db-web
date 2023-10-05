<template>
    <n-card title="" style="align-items: left">
        <n-space>
            <n-auto-complete
                    v-model:value="query_a_name"
                    placeholder="诗人姓名"
                    clearable
            />
            <n-button type="success" ghost style="" @click="search_author">查询</n-button>
            <n-button type="info" ghost @click="random_pick">
                随机
            </n-button>
        </n-space>
    </n-card>
    <n-table :bordered="false" :single-line="false" v-if="this.ready_render" style="margin-top: 2rem;">
        <thead>
        <tr>
            <th>姓名</th>
            <th>朝代</th>
            <th>操作</th>
        </tr>
        </thead>
        <tbody v-for="author in authors" :key="author.a_id">
        <tr>
            <td> {{ author.a_name }}</td>
            <td>{{ author.d_name }}</td>
            <td><n-button @click="view_author_poems(author.a_id)">查看TA的诗词</n-button></td>
        </tr>
        </tbody>
    </n-table>
</template>
    
<script>
    import { defineComponent} from 'vue'
    import { NButton, NAutoComplete, NSpace, NCard, NH2, NH3, NP, NH4, NBlockquote, NDivider, NCol, NIcon, NTable } from 'naive-ui';
    import axios from 'axios';
    import { ArrowBackCircleOutline as FrontIcon, ArrowForwardCircleOutline as BackIcon} from '@vicons/ionicons5'
    import router from "../router/index.js";
    export default defineComponent({
        components: {
            NTable, NButton, NCard, NAutoComplete, NSpace
        },
        methods: {
            random_pick: function() {
                axios.get( this.BASE_URL + "/display/author?" + "items_per_page=" + this.items_per_pag)
                .then((response) => {
                    this.authors = response.data
                    this.ready_render = true
                })
                .catch(function (error) {
                    console.log(error);
                });
            },
            search_author: function() {
                axios.get(this.BASE_URL + "/search/author?query_str=" + this.query_a_name + "&items_per_page=" + this.items_per_pag + "&curr_page=" + '1' )
                .then((response) => {
                    this.authors = response.data.result
                    this.ready_render = true
                })
                .catch(function (error) {
                    console.log(error);
                });
            },
            view_author_poems: function(id) {
                router.push('/search_poem_other_list/author/' + id)
            }
        }, mounted() {
            this.random_pick()
        }, data () {
            return {
                items_per_pag: 50,
                ready_render: false,
                authors: [],
                query_a_name: '',
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