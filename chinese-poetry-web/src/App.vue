<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
import { NLayout, NLayoutHeader, NLayoutContent, NDivider, NMessageProvider, NBackTop } from 'naive-ui';
</script>

<template>
  <n-message-provider>
  <n-layout>
      <n-layout-header><Header></Header></n-layout-header>
      <n-divider />
      <n-layout-content style="margin-top: 2rem;">
        <router-view></router-view>
      </n-layout-content>
  </n-layout>
</n-message-provider>
<n-back-top :right="50" />
</template>

<style scoped>

</style>
