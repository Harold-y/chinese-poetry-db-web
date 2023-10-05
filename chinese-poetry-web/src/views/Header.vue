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
      WineOutline as WineIcon
    } from '@vicons/ionicons5'
    function renderIcon(icon) {
      return () => h(NIcon, null, { default: () => h(icon) });
    }
    
    const menuOptions = [
      {
        label: () => h(
          "a",
          {
            href: "",
            target: "_blank",
            rel: "noopenner noreferrer"
          },
          "主页"
        ),
        key: "hear-the-wind-sing",
        icon: renderIcon(BookIcon)
      },
      {
        label: () => h(
          "a",
          {
            href: "",
            target: "_blank",
            rel: "noopenner noreferrer"
          },
          "搜索"
        ),
        key: "hear-the-wind-sing",
        icon: renderIcon(BookIcon)
      },
      {
        label: () => h(
          "a",
          {
            href: "",
            target: "_blank",
            rel: "noopenner noreferrer"
          },
          "词牌/韵律"
        ),
        key: "hear-the-wind-sing",
        icon: renderIcon(BookIcon)
      },
      {
        label: () => h(
          "a",
          {
            href: "",
            target: "_blank",
            rel: "noopenner noreferrer"
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