<template>
<Header></Header>
</template>

<script>
  import Header from '../views/Header.vue'
  import { defineComponent } from 'vue'
  export default defineComponent({
    components: {
      Header
    },
    methods: {

    }, mounted() {

    }, data () {
      return {
        jobs: [],
        
      }
    }, setup() {
    return {
      
    };
  }
  })
</script>

<style>

</style>