<template>
  <div>
    <h1>Courses</h1>

    <input
      v-model="searchTerm"
      placeholder="Search courses..."
    />

    <CourseCard
      v-for="course in filteredCourses"
      :key="course.id"
      :name="course.name"
      :code="course.code"
      :credits="course.credits"
      :grade="course.grade"
      @enroll="enrollCourse(course)"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import CourseCard from "../components/CourseCard.vue";
import { useEnrollmentStore } from "../stores/enrollment";
import { getAllCourses } from "../api/courseApi";

const store = useEnrollmentStore();

const searchTerm = ref("");
const courses = ref([]);

onMounted(async () => {
  try {
    const data = await getAllCourses();

    courses.value = data.slice(0, 5).map((item) => ({
      id: item.id,
      name: item.title,
      code: `C${item.id}`,
      credits: 3,
      grade: "A",
    }));
  } catch (error) {
    console.error("Error loading courses:", error);
  }
});

const filteredCourses = computed(() =>
  courses.value.filter((course) =>
    course.name
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase())
  )
);

function enrollCourse(course) {
  store.enroll(course);
}
</script>

<style scoped>
input {
  padding: 8px;
  margin-bottom: 15px;
  width: 250px;
}
</style>