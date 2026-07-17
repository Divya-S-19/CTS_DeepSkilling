import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

function Header() {
  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <nav>
      <h2>Student Portal</h2>

      <Link to="/">Home</Link> |{" "}
      <Link to="/courses">Courses</Link> |{" "}
      <Link to="/profile">
        Profile ({enrolledCourses.length})
      </Link>
    </nav>
  );
}

export default Header;