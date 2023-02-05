<script setup>
import AppIntroduction from "@/components/AppIntroduction.vue";
import AuthorCredits from "@/components/AuthorCredits.vue";
import InputForm from "@/components/InputForm.vue";
import DarkToggle from "@/components/DarkToggle.vue";</script>

<template>
  <DarkToggle class="absolute top-4 right-4 lg:top-8 lg:right-8"/>
  <div class="flex flex-col lg:grid lg:grid-cols-2 gap-4 lg:gap-8 max-w-7xl mx-auto pb-4 lg:pb-0">
    <div class="flex flex-col gap-4">
      <AppIntroduction/>
      <AuthorCredits/>
    </div>

    <main>
      <InputForm/>
    </main>
  </div>
</template>

