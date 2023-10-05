<template>
    <n-table :bordered="false" :single-line="false" v-if="this.ready_render">
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
            axios.get( this.BASE_URL + "/display/author?" + "items_per_page=" + this.items_per_pag)
                .then((response) => {
                    this.authors = response.data.result
                    this.ready_render = true
                })
                .catch(function (error) {
                    console.log(error);
                });
        }, data () {
            return {
                items_per_pag: 50,
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