import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { getCourseById, enrollStudent } from "../api/courseApi";

export const useEnrollmentStore = defineStore("enrollment", () => {
  const enrolledCourses = ref([]);
  const loading = ref(false);
  const error = ref(null);

  function enroll(course) {
    enrolledCourses.value.push(course);
  }

  function unenroll(id) {
    enrolledCourses.value = enrolledCourses.value.filter(
      (c) => c.id !== id
    );
  }

  const totalCredits = computed(() =>
    enrolledCourses.value.reduce(
      (sum, c) => sum + c.credits,
      0
    )
  );

  // Task 149
  async function fetchAndEnroll(courseId) {
    try {
      loading.value = true;
      error.value = null;

      const course = await getCourseById(courseId);

      await enrollStudent(1, courseId);

      enrolledCourses.value.push(course);
    } catch (err) {
      error.value = err.message;
    } finally {
      loading.value = false;
    }
  }

  // Task 149
  function resetEnrollment() {
    enrolledCourses.value = [];
    loading.value = false;
    error.value = null;
  }

  return {
    enrolledCourses,
    loading,
    error,
    enroll,
    unenroll,
    fetchAndEnroll,
    resetEnrollment,
    totalCredits,
  };
});