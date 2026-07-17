<template>
  <div>
    <h1>Profile</h1>

    <p>Total Credits: {{ store.totalCredits }}</p>

    <p v-if="loading">Loading...</p>

    <p v-if="error">{{ error }}</p>

    <div v-for="c in enrolledCourses" :key="c.id">
      {{ c.name }} - {{ c.code }}
    </div>
  </div>
</template>

<script setup>
import { useEnrollmentStore } from "../stores/enrollment";
import { storeToRefs } from "pinia";

const store = useEnrollmentStore();

const {
  enrolledCourses,
  loading,
  error
} = storeToRefs(store);
</script>