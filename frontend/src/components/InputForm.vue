<template>
  <div class="flex flex-col gap-8">
    <div class="flex flex-col gap-4">
      <div>
        <textarea id="email_text"
                  v-model="emailText"
                  class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 dark:bg-zinc-700 dark:border-zinc-600 dark:placeholder-gray-400 dark:text-white"
                  placeholder="Paste the text of an email here"
                  rows="16"></textarea>
      </div>
      <div class="flex w-full gap-2">
        <button class="bg-purple-500 hover:bg-purple-600 focus:ring-4 ring-purple-300 p-2.5 text-white rounded-lg grow"
                @click="getEmailClass">Submit
        </button>
        <button @click="setSampleEmail('non-spam')" class="bg-purple-500 hover:bg-purple-600 focus:ring-4 ring-purple-300 p-2 5 text-white rounded-lg aspect-square">
          <svg class="mx-auto" width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M22 8.608v8.142a3.25 3.25 0 0 1-3.066 3.245L18.75 20H5.25a3.25 3.25 0 0 1-3.245-3.066L2 16.75V8.608l9.652 5.056a.75.75 0 0 0 .696 0L22 8.608ZM5.25 4h13.5a3.25 3.25 0 0 1 3.234 2.924L12 12.154l-9.984-5.23a3.25 3.25 0 0 1 3.048-2.919L5.25 4h13.5-13.5Z" fill="#fff"/></svg>
        </button>
        <button @click="setSampleEmail('spam')" class="bg-purple-500 hover:bg-purple-600 focus:ring-4 ring-purple-300 p-2 5 text-white rounded-lg aspect-square">
          <svg class="mx-auto" width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0Zm-9.5 0c0 .834.255 1.608.691 2.248l5.557-5.557A4 4 0 0 0 13.5 6.5Zm4 4a4 4 0 0 0 3.309-6.248l-5.557 5.557c.64.436 1.414.691 2.248.691Zm0 2.5a6.478 6.478 0 0 0 4.5-1.81v5.56a3.25 3.25 0 0 1-3.066 3.245L18.75 20H5.25a3.25 3.25 0 0 1-3.245-3.066L2 16.75V8.608l9.652 5.056a.75.75 0 0 0 .696 0l2.417-1.266A6.477 6.477 0 0 0 17.5 13ZM5.25 4h6.248A6.479 6.479 0 0 0 11 6.5c0 1.993.897 3.776 2.308 4.968L12 12.153l-9.984-5.23a3.25 3.25 0 0 1 3.048-2.918L5.25 4Z" fill="#fff"/></svg>
        </button>
      </div>
    </div>
    <ResultDisplay :result="result"/>
  </div>
</template>

<script>
import ResultDisplay from "@/components/ResultDisplay.vue";
import emails from "@/assets/sample-emails.json";

export default {
  name: "InputForm",
  components: {ResultDisplay},
  data() {
    return {
      emailText: "",
      result: ""
    }
  },
  methods: {
    getEmailClass() {
      fetch('http://localhost:8000/spam/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          text: this.emailText
        })
      })
          .then(response => response.json())
          .then(data => {
            this.result = data.label
          })
    },
    setSampleEmail(type) {
      this.emailText = emails[type]
    }
  },
  watch: {
    emailText: function () {
      this.result = "";
    }
  }
}


</script>

<style scoped>

</style>