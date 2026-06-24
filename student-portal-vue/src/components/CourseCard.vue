<template>
  <div class="card">
    <h3>{{ name }}</h3>
    <p>Code: {{ code }}</p>
    <p>Credits: {{ credits }}</p>
    <p>Grade: {{ grade }}</p>

    <button @click="$emit('enroll')">Enroll</button>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
});
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 12px;
  margin: 10px;
}
</style>