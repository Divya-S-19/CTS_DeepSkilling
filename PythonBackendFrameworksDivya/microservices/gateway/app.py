from flask import Flask, request, Response
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://localhost:5001"
STUDENT_SERVICE = "http://localhost:5002"


@app.route("/api/courses", methods=["GET", "POST"])
def courses():
    response = requests.request(
        method=request.method,
        url=f"{COURSE_SERVICE}/api/courses",
        json=request.get_json(silent=True)
    )
    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get("Content-Type")
    )


@app.route("/api/students", methods=["GET", "POST"])
def students():
    response = requests.request(
        method=request.method,
        url=f"{STUDENT_SERVICE}/api/students",
        json=request.get_json(silent=True)
    )
    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get("Content-Type")
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)