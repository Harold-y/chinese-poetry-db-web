<template>
    <n-menu v-model:value="activeKey" mode="horizontal" :options="menuOptions" />
</template>
    
    <script>
      import { defineComponent, h, ref } from 'vue'
      import { NButton, NCollapseItem, NCollapse, NMenu, NAutoComplete, NPageHeader } from 'naive-ui'
      import { NIcon } from 'naive-ui'
      import {
      BookOutline as BookIcon,
      PersonOutline as PersonIcon,
      ReaderOutline as ReaderIcon,
      SearchOutline as SearchIcon,
      HomeOutline as HomeIcon
    } from '@vicons/ionicons5'
    import { RouterLink } from 'vue-router'
    function renderIcon(icon) {
      return () => h(NIcon, null, { default: () => h(icon) });
    }
    
    const menuOptions = [
      {
        label: () => h(
          RouterLink,
          {
            to: {
              name: 'home',
              params: {

              }
            }
          },
          "主页"
        ),
        key: "hear-the-wind-sing",
        icon: renderIcon(HomeIcon)
      },
      {
        label: () => h(
          RouterLink,
          {
            to: {
              name: 'search',
              params: {
                
              }
            }
          },
          "搜索"
        ),
        key: "hear-the-wind-sing",
        icon: renderIcon(SearchIcon)
      },
      {
        label: () => h(
          RouterLink,
          {
            to: {
              name: 'author',
              params: {
                
              }
            }
          },
          "诗人"
        ),
        key: "hear-the-wind-sing",
        icon: renderIcon(PersonIcon)
      },
      {
        label: () => h(
          RouterLink,
          {
            to: {
              name: 'rhythmic',
              params: {
                
              }
            }
          },
          "词牌/韵律"
        ),
        key: "hear-the-wind-sing",
        icon: renderIcon(ReaderIcon)
      },
      {
        label: () => h(
          RouterLink,
          {
            to: {
              name: 'collection',
              params: {
                
              }
            }
          },
          "诗集"
        ),
        key: "hear-the-wind-sing",
        icon: renderIcon(BookIcon)
      },
    ];
    
      export default defineComponent({
        components: {
          NButton, NCollapseItem, NCollapse, NMenu, NAutoComplete, NPageHeader
        },
        methods: {
    
        }, mounted() {
    
        }, data () {
          return {
            jobs: [],
            menuOptions: menuOptions
          }
        }, setup() {
        return {
          activeKey: ref(null),
          menuOptions
        };
      }, props: {

      }
      })
    </script>
    
    <style>
    
    </style>