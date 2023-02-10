<template>
  <button
      class="transition-colors border-2 border-gray-200 rounded-lg p-2 hover:bg-gray-200 dark:hover:bg-gray-200 fill-gray-400 hover:fill-zinc-800 dark:fill-white dark:hover:fill-zinc-800"
      @click="toggleDark()">
    <IconMoon v-if="isDark"/>
    <IconSun v-else/>
  </button>
</template>

<script>
export default {
  name: "DarkToggle"
}
</script>

<script setup>
import {useDark, useToggle} from '@vueuse/core';
import IconMoon from "@/components/icons/IconMoon.vue";
import IconSun from "@/components/icons/IconSun.vue";

const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>