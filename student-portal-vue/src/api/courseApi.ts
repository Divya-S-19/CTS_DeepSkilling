import apiClient from "./apiClient";

export const getAllCourses = () => {
  return apiClient.get("/posts");
};

export const getCourseById = (id: number) => {
  return apiClient.get(`/posts/${id}`);
};

export const enrollStudent = (
  studentId: number,
  courseId: number
) => {
  return apiClient.post("/posts", {
    studentId,
    courseId,
  });
};