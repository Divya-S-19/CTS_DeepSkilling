from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Student Service Running"


@app.route("/api/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    return jsonify([
        {
            "id": s.id,
            "name": s.name
        }
        for s in students
    ])


@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.json

    student = Student(name=data["name"])

    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student Added"}), 201


# Enrollment Endpoint
@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll(id):

    data = request.json
    course_id = data["course_id"]

    try:
        response = requests.get(
            f"http://localhost:5001/api/courses/{course_id}"
        )

        if response.status_code == 404:
            return jsonify({"message": "Course Not Found"}), 404

        return jsonify({
            "message": f"Student {id} enrolled in Course {course_id}"
        })

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service Unavailable"
        }), 503


# Temporary route to add a student
@app.route("/addstudent")
def add_student_sample():
    student = Student(name="Divya")

    db.session.add(student)
    db.session.commit()

    return "Student Added"


# Temporary route to test enrollment
@app.route("/testenroll")
def test_enroll():
    try:
        response = requests.get("http://localhost:5001/api/courses/1")

        if response.status_code == 404:
            return "Course Not Found"

        return "Student 1 enrolled in Course 1"

    except requests.exceptions.ConnectionError:
        return "Course Service Unavailable"


if __name__ == "__main__":
    app.run(port=5002, debug=True)