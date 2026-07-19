from flask import Flask, request, jsonify
from models import db, Course

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# Home Route
@app.route("/")
def home():
    return "Course Service Running"


# Get All Courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])


# Get One Course
@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course Not Found"}), 404

    return jsonify(course.to_dict())


# Add Course
@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.json

    course = Course(
        name=data["name"],
        department=data["department"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify({
        "message": "Course Added"
    }), 201


# Add Sample Course (Temporary)
@app.route("/addsample")
def add_sample():
    course = Course(
        name="Python",
        department="IT"
    )

    db.session.add(course)
    db.session.commit()

    return "Sample Course Added"


if __name__ == "__main__":
    app.run(port=5001, debug=True)