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
          <IconEmail class="mx-auto"/>
        </button>
        <button @click="setSampleEmail('spam')" class="bg-purple-500 hover:bg-purple-600 focus:ring-4 ring-purple-300 p-2 5 text-white rounded-lg aspect-square">
          <IconEmailSpam class="mx-auto"/>
        </button>
      </div>
    </div>
    <ResultDisplay :result="result"/>
  </div>
</template>

<script>
import ResultDisplay from "@/components/ResultDisplay.vue";
import emails from "@/assets/sample-emails.json";
import IconEmail from "@/components/icons/IconEmail.vue";
import IconEmailSpam from "@/components/icons/IconEmailSpam.vue";

export default {
  name: "InputForm",
  components: {IconEmailSpam, IconEmail, ResultDisplay},
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

