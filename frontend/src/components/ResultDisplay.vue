<template>
  <div
      class="p-2 py-6 border border-gray-300 rounded-lg bg-gray-50 text-center text-gray-700 dark:bg-zinc-700 dark:border-zinc-600 dark:text-gray-200">
    <p v-if="!result">Results will appear here</p>
    <p v-if="result">Email classified as <span class="text-purple-500 font-semibold">{{ result }}</span></p>
  </div>
</template>

<script>
export default {
  name: "ResultDisplay",
  props: {result: String}
}
</script>

<style scoped>

</style>