import { Link } from "react-router-dom";

function CoursesPage() {
  const courses = [
    { id: 1, name: "Data Structures" },
    { id: 2, name: "Database Management" },
    { id: 3, name: "Web Development" },
    { id: 4, name: "Python Programming" },
    { id: 5, name: "Artificial Intelligence" }
  ];

  return (
    <div>
      <h2>Courses</h2>

      {courses.map((course) => (
        <div key={course.id}>
          <Link to={`/courses/${course.id}`}>
            {course.name}
          </Link>
        </div>
      ))}
    </div>
  );
}

export default CoursesPage;