import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";

function CourseCard({ id, name, code, credits }) {
  const dispatch = useDispatch();

  const handleEnroll = () => {
    dispatch(
      enroll({
        id,
        name,
        code,
        credits,
      })
    );
  };

  return (
    <div>
      <h3>{name}</h3>
      <p>Code: {code}</p>
      <p>Credits: {credits}</p>

      <button onClick={handleEnroll}>
        Enroll
      </button>
    </div>
  );
}

export default CourseCard;