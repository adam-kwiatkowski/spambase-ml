<template>
  <button
      class="transition-colors border-2 border-gray-200 rounded-lg p-2 hover:bg-gray-200 dark:hover:bg-gray-200 fill-gray-400 hover:fill-zinc-800 dark:fill-white dark:hover:fill-zinc-800"
      @click="toggleDark()">
    <svg v-if="isDark" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
      <path
          d="M20.026 17.001c-2.762 4.784-8.879 6.423-13.663 3.661A9.965 9.965 0 0 1 3.13 17.68a.75.75 0 0 1 .365-1.132c3.767-1.348 5.785-2.91 6.956-5.146 1.232-2.353 1.551-4.93.689-8.463a.75.75 0 0 1 .769-.927 9.961 9.961 0 0 1 4.457 1.327c4.784 2.762 6.423 8.879 3.66 13.662Z"/>
    </svg>
    <svg v-else height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
      <path
          d="M11.996 19.01a.75.75 0 0 1 .743.649l.007.102v1.5a.75.75 0 0 1-1.493.101l-.007-.101v-1.5a.75.75 0 0 1 .75-.75Zm6.022-2.072 1.06 1.06a.75.75 0 1 1-1.06 1.061l-1.06-1.06a.75.75 0 0 1 1.06-1.061Zm-10.983 0a.75.75 0 0 1 0 1.06L5.974 19.06a.75.75 0 0 1-1.06-1.06l1.06-1.061a.75.75 0 0 1 1.06 0ZM12 6.475a5.525 5.525 0 1 1 0 11.05 5.525 5.525 0 0 1 0-11.05Zm0 1.5a4.025 4.025 0 1 0 0 8.05 4.025 4.025 0 0 0 0-8.05Zm9.25 3.293a.75.75 0 0 1 .102 1.493l-.102.007h-1.5a.75.75 0 0 1-.102-1.493l.102-.007h1.5Zm-17-.029a.75.75 0 0 1 .102 1.494l-.102.006h-1.5a.75.75 0 0 1-.102-1.493l.102-.007h1.5Zm1.64-6.37.084.072 1.06 1.06a.75.75 0 0 1-.976 1.134l-.084-.073-1.06-1.06a.75.75 0 0 1 .976-1.134Zm13.188.072a.75.75 0 0 1 .073.977l-.073.084-1.06 1.06a.75.75 0 0 1-1.133-.976l.072-.084 1.06-1.061a.75.75 0 0 1 1.061 0ZM12 1.99a.75.75 0 0 1 .743.648l.007.102v1.5a.75.75 0 0 1-1.493.101l-.007-.102v-1.5a.75.75 0 0 1 .75-.75Z"/>
    </svg>
  </button>
</template>

<script>
export default {
  name: "DarkToggle"
}
</script>

<script setup>
import {useDark, useToggle} from '@vueuse/core';

const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>