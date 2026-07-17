from flask import Blueprint, request, jsonify
from extensions import db
from .models import Course, Enrollment

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


def make_response_json(data, status_code):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


# GET ALL COURSES
@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return make_response_json([course.to_dict() for course in courses], 200)


# CREATE COURSE
@courses_bp.route("/", methods=["POST"])
def add_course():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request must be JSON"}), 400

    required = ["name", "code", "credits", "department_id"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return make_response_json(course.to_dict(), 201)


# GET ONE COURSE
@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict(), 200)


# UPDATE COURSE
@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)

    data = request.get_json()

    course.name = data.get("name", course.name)
    course.code = data.get("code", course.code)
    course.credits = data.get("credits", course.credits)

    db.session.commit()

    return make_response_json(course.to_dict(), 200)


# DELETE COURSE
@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted"}), 200


# GET STUDENTS ENROLLED IN A COURSE
@courses_bp.route("/<int:course_id>/students/", methods=["GET"])
def get_students(course_id):

    enrollments = Enrollment.query.filter_by(course_id=course_id).all()

    students = [enrollment.student.to_dict() for enrollment in enrollments]

    return make_response_json(students, 200)