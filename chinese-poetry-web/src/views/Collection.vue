<template>
    <div v-for="collection in collections" :key="collection.c_id">
        <n-card title="" style="padding: 1rem; margin-top: 1rem;" @click="() => {this.view_collection_poems(collection.c_id)}">
                <n-h2>{{ collection.c_name }}</n-h2>
                <n-p>{{ collection.c_note }}</n-p>
        </n-card>        
    </div>
</template>
    
<script>
    import { defineComponent} from 'vue'
    import { NButton, NAutoComplete, NSpace, NCard, NH2, NH3, NP, NH4, NBlockquote, NDivider, NCol, NIcon, NTable } from 'naive-ui';
    import axios from 'axios';
    import router from "../router/index.js";
    export default defineComponent({
        components: {
            NTable, NButton, NCard, NAutoComplete, NSpace, NH2, NP
        },
        methods: {
            view_collection_poems: function(id) {
                router.push('/search_poem_other_list/collection/' + id)
            }
        }, mounted() {
            axios.get( this.BASE_URL + "/display/collection")
                .then((response) => {
                    this.collections = response.data
                    this.ready_render = true
                })
                .catch(function (error) {
                    console.log(error);
                });
        }, data () {
            return {
                ready_render: false,
                collections: [],
            }
        }, setup() {
            return {
                
            };
        }, props: {
        
        }
    })

</script>

<style scoped>
.n-card:hover {
    transition-duration: 0.7s;
    border-color: #18a058;
    cursor: pointer;
}
</style>