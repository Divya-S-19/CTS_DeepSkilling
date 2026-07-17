<template>
  <div>
    <h2>Course Detail</h2>
    <p>Course ID: {{ route.params.id }}</p>

    <button @click="goProfile">Enroll</button>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

function goProfile() {
  router.push("/profile");
}
</script>