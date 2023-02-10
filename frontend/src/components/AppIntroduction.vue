<template>
  <div class="flex flex-col gap-4">
    <div class="flex flex-row items-center">
      <IconEmailSpam class="bg-purple-500 rounded-2xl p-2 mr-2" fill="#fff" height="48" width="48"/>
      <h1 class="text-4xl lg:text-5xl">Spam detector</h1>
    </div>
    <div class="text-gray-600 dark:text-gray-200">
      <p>
        This application utilizes a Random Forest classifier to label emails as spam or not spam. The model
        has been trained and tested on the Spambase dataset, which consists of over 4600 emails and 57 features. The
        dataset is publicly available at the <a href="https://archive.ics.uci.edu/ml/datasets/Spambase">UCI Machine
        Learning Repository</a>.
      </p>
      <br>
      <p>
        Random Forest is a widely used machine learning algorithm, especially for binary classification tasks such as
        spam detection. It works by creating an ensemble of decision trees to make predictions. The classifier considers
        multiple features and determines the class of an email by aggregating the predictions made by each tree.
      </p>
    </div>
  </div>
</template>

<script>
import IconEmailSpam from "@/components/icons/IconEmailSpam.vue";

export default {
  name: "AppIntroduction",
  components: {IconEmailSpam},
}
</script>

<style scoped>
a {
  @apply text-purple-500;
}
</style>
