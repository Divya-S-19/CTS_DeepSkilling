import { useSelector, useDispatch } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {
  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <div>
      <h2>Enrolled Courses</h2>

      {enrolledCourses.length === 0 ? (
        <p>No courses enrolled.</p>
      ) : (
        enrolledCourses.map((course) => (
          <div key={course.id}>
            <p>{course.name}</p>

            <button
              onClick={() => dispatch(unenroll(course.id))}
            >
              Remove
            </button>
          </div>
        ))
      )}
    </div>
  );
}

export default ProfilePage;