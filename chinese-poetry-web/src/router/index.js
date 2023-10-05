import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Author from '../views/Author.vue'
import Collection from '../views/Collection.vue'
import Rhythmic from '../views/Rhythmic.vue'
import Search from '../views/Search.vue'
import PoemSearchList from '../views/PoemSearchList.vue'
import Poem from '../components/Poem.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/author',
      name: 'author',
      component: Author
    },
    {
      path: '/collection',
      name: 'collection',
      component: Collection
    },
    {
      path: '/rhythmic',
      name: 'rhythmic',
      component: Rhythmic
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    },
    {
      path: '/search_poem_list/:query_method/:query_text',
      name: 'searchPoemList',
      component: PoemSearchList,
      props: true
    },
    {
      path: '/poem/:poem_id',
      name: 'poemDetail',
      component: Poem,
      props: true
    },
    
  ]
})

export default router
