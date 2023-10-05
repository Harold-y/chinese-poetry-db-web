<template>
<Poem v-if = "this.show_poem" :poem_info="this.random_poem_info"/>
</template>

<script>
  
  import { defineComponent } from 'vue'
  import Poem from '../components/Poem.vue'
  import axios from 'axios'
  export default defineComponent({
    components: {
      Poem
    },
    methods: {

    }, async mounted() {
      await axios.get( this.BASE_URL + "/query/random_poem")
        .then((response) => {
            this.random_poem_info = response.data
            this.show_poem = true
        })
        .catch(function (error) {
            console.log(error);
        });
        
    }, data () {
      return {
        random_poem_info: {},
        show_poem: false
      }
    }, setup() {
    return {
      
    };
  }
  })
</script>

<style>

</style>