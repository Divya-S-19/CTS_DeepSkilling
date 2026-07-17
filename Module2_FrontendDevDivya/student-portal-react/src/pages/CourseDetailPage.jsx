import { useParams, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";

function CourseDetailPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const courses = [
    { id: 1, name: "Data Structures", code: "CS101", credits: 4 },
    { id: 2, name: "Database Management", code: "CS102", credits: 3 },
    { id: 3, name: "Web Development", code: "CS103", credits: 4 },
    { id: 4, name: "Python Programming", code: "CS104", credits: 4 },
    { id: 5, name: "Artificial Intelligence", code: "CS105", credits: 3 }
  ];

  const course = courses.find(
    (c) => c.id === Number(courseId)
  );

  if (!course) {
    return <h2>Course Not Found</h2>;
  }

  const handleEnroll = () => {
    dispatch(enroll(course));
    navigate("/profile");
  };

  return (
    <div>
      <h2>{course.name}</h2>
      <p>Code: {course.code}</p>
      <p>Credits: {course.credits}</p>

      <button onClick={handleEnroll}>
        Enroll
      </button>
    </div>
  );
}

export default CourseDetailPage;