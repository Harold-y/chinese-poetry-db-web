<template>
    <n-table :bordered="false" :single-line="false">
        <thead>
        <tr>
            <th>姓名</th>
            <th>朝代</th>
            <th>操作</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>放弃</td>
            <td>反常的</td>
            <td>彻底废除</td>
        </tr>
        </tbody>
    </n-table>
</template>
    
<script>
    import { defineComponent} from 'vue'
    import { NButton, NGrid, NGi, NSpace, NCard, NH2, NH3, NP, NH4, NBlockquote, NDivider, NCol, NIcon, NTable } from 'naive-ui';
    import axios from 'axios';
    import { ArrowBackCircleOutline as FrontIcon, ArrowForwardCircleOutline as BackIcon} from '@vicons/ionicons5'
    import router from "../router/index.js";
    export default defineComponent({
        components: {
            NTable
        },
        methods: {

        }, mounted() {
            axios.get( this.BASE_URL + "/search/poem?query_type=" + this.query_method + "&query_str=" + this.query_text + "&items_per_page=" + this.items_per_pag + "&curr_page=" + this.curr_page)
                .then((response) => {
                    this.poem_list = response.data.result
                    this.poem_list_length = response.data.num_res
                    for (var i = 0; i < this.poem_list_length; i ++)
                    {
                        this.clean_data(this.poem_list[i])
                    }
                    if (this.poem_list_length < this.items_per_pag) {
                        this.next_disabled = true
                    }
                    this.loaded = true
                })
                .catch(function (error) {
                    console.log(error);
                });
        }, data () {
            return {
                ready_render: false,
                authors: [],            
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