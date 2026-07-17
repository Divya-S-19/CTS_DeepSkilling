"""
N+1 Problem Analysis

Without joinedload():
One query loads enrollments and additional queries load
student and course data. This causes the N+1 problem.

With joinedload():
Student and course data are loaded using JOINs in a
single SQL query, improving performance significantly.
"""
from datetime import date
from sqlalchemy.orm import sessionmaker, joinedload
from models import engine, Department, Student, Course, Enrollment

Session = sessionmaker(bind=engine)
session = Session()

# -------------------------
# INSERT Departments
# -------------------------
cs = Department(
    dept_name="Computer Science",
    head_of_dept="Dr. Kumar",
    budget=900000
)

ece = Department(
    dept_name="Electronics",
    head_of_dept="Dr. Priya",
    budget=700000
)

mech = Department(
    dept_name="Mechanical",
    head_of_dept="Dr. Suresh",
    budget=600000
)

session.add_all([cs, ece, mech])

try:
    session.commit()
except:
    session.rollback()

# -------------------------
# INSERT Students
# -------------------------
students = [
    Student(
        first_name="Rahul",
        last_name="Kumar",
        email="rahul.orm1@gmail.com",
        date_of_birth=date(2003,5,10),
        department_id=1,
        enrollment_year=2022
    ),
    Student(
        first_name="Anjali",
        last_name="Sharma",
        email="anjali.orm1@gmail.com",
        date_of_birth=date(2004,2,15),
        department_id=1,
        enrollment_year=2023
    )
]

session.add_all(students)

try:
    session.commit()
except:
    session.rollback()

# -------------------------
# READ Students
# -------------------------
print("\nStudents in Computer Science\n")

results = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

for s in results:
    print(s.first_name, s.last_name)

# -------------------------
# READ Enrollments using joinedload
# -------------------------
print("\nUsing joinedload()\n")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        "->",
        e.course.course_name
    )
# -------------------------
# UPDATE
# -------------------------
student = (
    session.query(Student)
    .filter(Student.email == "rahul.orm1@gmail.com")
    .first()
)

if student:
    student.enrollment_year = 2024
    session.commit()
    print("\nStudent Updated")

# -------------------------
# DELETE
# -------------------------
enrollment = session.query(Enrollment).first()

if enrollment:
    session.delete(enrollment)
    session.commit()
    print("One enrollment deleted")

session.close()