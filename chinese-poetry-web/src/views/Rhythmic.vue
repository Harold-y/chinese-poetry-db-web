<template>
    <n-card title="" style="align-items: left">
        <n-space>
            <n-auto-complete
                    v-model:value="query_r_name"
                    placeholder="词牌/韵律"
                    clearable
            />
            <n-button type="success" ghost style="" @click="search_rhy">查询</n-button>
            <n-button type="info" ghost @click="random_pick">
                随机
            </n-button>
        </n-space>
    </n-card>
    <n-table :bordered="false" :single-line="false" v-if="this.ready_render" style="margin-top: 2rem;">
        <thead>
        <tr>
            <th>名称</th>
            <th>注释</th>
            <th>操作</th>
        </tr>
        </thead>
        <tbody v-for="rhy in rhys" :key="rhy.r_id">
        <tr>
            <td> {{ rhy.r_name }}</td>
            <td>{{ rhy.r_note }}</td>
            <td><n-button @click="view_rhy_poems(rhy.r_id)">其它此词牌诗词</n-button></td>
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
                axios.get( this.BASE_URL + "/display/rhythmic?" + "items_per_page=" + this.items_per_pag)
                .then((response) => {
                    this.rhys = response.data
                    this.ready_render = true
                })
                .catch(function (error) {
                    console.log(error);
                });
            },
            search_rhy: function() {
                axios.get(this.BASE_URL + "/search/rhythmic?r_name=" + this.query_r_name + "&items_per_page=" + this.items_per_pag + "&curr_page=" + '1' )
                .then((response) => {
                    this.rhys = response.data.result
                    this.ready_render = true
                })
                .catch(function (error) {
                    console.log(error);
                });
            },
            view_rhy_poems: function(id) {
                router.push('/search_poem_other_list/rhy/' + id)
            }
        }, mounted() {
            this.random_pick()
        }, data () {
            return {
                items_per_pag: 50,
                ready_render: false,
                rhys: [],
                query_r_name: '',
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