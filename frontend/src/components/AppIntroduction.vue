<template>
  <div class="flex flex-col gap-4">
    <div class="flex flex-row items-center">
      <svg class="bg-purple-500 rounded-2xl p-2 mr-2" fill="none" height="48" viewBox="0 0 24 24" width="48"
           xmlns="http://www.w3.org/2000/svg">
        <path
            d="M23 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0Zm-9.5 0c0 .834.255 1.608.691 2.248l5.557-5.557A4 4 0 0 0 13.5 6.5Zm4 4a4 4 0 0 0 3.309-6.248l-5.557 5.557c.64.436 1.414.691 2.248.691Zm0 2.5a6.478 6.478 0 0 0 4.5-1.81v5.56a3.25 3.25 0 0 1-3.066 3.245L18.75 20H5.25a3.25 3.25 0 0 1-3.245-3.066L2 16.75V8.608l9.652 5.056a.75.75 0 0 0 .696 0l2.417-1.266A6.477 6.477 0 0 0 17.5 13ZM5.25 4h6.248A6.479 6.479 0 0 0 11 6.5c0 1.993.897 3.776 2.308 4.968L12 12.153l-9.984-5.23a3.25 3.25 0 0 1 3.048-2.918L5.25 4Z"
            fill="#fefaf1"/>
      </svg>
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
export default {
  name: "AppIntroduction",
}
</script>

<style scoped>
a {
  @apply text-purple-500;
}
</style>
