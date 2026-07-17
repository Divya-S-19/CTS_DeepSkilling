from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_
from security import get_password_hash, verify_password
from models import User
from schemas import UserRegister

from database import get_db, init_db

from schemas import (
    CourseCreate,
    CourseResponse,
    CourseUpdate,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse,
    UserRegister,
    UserLogin,
    UserResponse
)
from models import Student, Enrollment, Course, User
# API Versioning
# URL Versioning: /api/v1/students/ (easy to understand and test)
# Header Versioning: Accept: application/vnd.api+json;version=1
# URL versioning is used in this project.
app = FastAPI(
    title="Course Management API",
    description="API for managing courses, students and enrollments using FastAPI and Async SQLAlchemy.",
    version="1.0.0",
    contact={
        "name": "Divya",
        "email": "divya@example.com"
    }
)
@app.on_event("startup")
async def startup():
    await init_db()


# ----------------------------
# Background Task
# ----------------------------

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


# =====================================================
# STUDENT CRUD
# =====================================================

# CREATE STUDENT
@app.post(
    "/api/v1/students/",
    tags=["Students"],
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_student(
    student: StudentCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)

    await db.commit()

    await db.refresh(new_student)
    response.headers["Location"] = f"/api/v1/students/{new_student.id}"

    return new_student


# GET ALL STUDENTS
@app.get(
    "/api/v1/students/",
    tags=["Students"],
    response_model=list[StudentResponse]
)
async def get_students(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(select(Student))

    return result.scalars().all()


# GET STUDENT BY ID
@app.get(
    "/api/v1/students/{student_id}",
    tags=["Students"],
    response_model=StudentResponse
)
async def get_student(
    student_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# UPDATE STUDENT
@app.put(
    "/api/v1/students/{student_id}",
    tags=["Students"],
    response_model=StudentResponse
)
async def update_student(
    student_id: int,
    student: StudentCreate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    existing_student = result.scalar_one_or_none()

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    existing_student.name = student.name
    existing_student.email = student.email

    await db.commit()

    await db.refresh(existing_student)

    return existing_student


# DELETE STUDENT
@app.delete(
    "/api/v1/students/{student_id}",
    tags=["Students"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": f"Student with id {student_id} does not exist",
            "field": None
        }
    }
)

    await db.delete(student)

    await db.commit()


# =====================================================
# ENROLLMENT CRUD
# =====================================================

# CREATE ENROLLMENT
@app.post(
    "/api/v1/enrollments/",
    tags=["Enrollments"],
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    response: Response,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):

    new_enrollment = Enrollment(
        course_id=enrollment.course_id,
        student_id=enrollment.student_id
    )

    db.add(new_enrollment)

    await db.commit()

    await db.refresh(new_enrollment)
    response.headers["Location"] = f"/api/v1/enrollments/{new_enrollment.id}"

    background_tasks.add_task(
        send_confirmation_email,
        "student@example.com"
    )

    return new_enrollment


# GET ALL ENROLLMENTS
@app.get(
    "/api/v1/enrollments/",
    tags=["Enrollments"],
    response_model=list[EnrollmentResponse]
)
async def get_enrollments(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(select(Enrollment))

    return result.scalars().all()


# GET ENROLLMENT BY ID
@app.get(
    "/api/v1/enrollments/{enrollment_id}",
    tags=["Enrollments"],
    response_model=EnrollmentResponse
)
async def get_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
       raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": f"Enrollment with id {enrollment_id} does not exist",
            "field": None
        }
    }
)

    return enrollment


# DELETE ENROLLMENT
@app.delete(
    "/api/v1/enrollments/{enrollment_id}",
    tags=["Enrollments"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    await db.delete(enrollment)

    await db.commit()
@app.patch(
    "/api/v1/courses/{course_id}",
    tags=["Courses"],
    response_model=CourseResponse
)
async def patch_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    existing_course = result.scalar_one_or_none()

    if existing_course is None:
        raise HTTPException(
    status_code=404,
    detail={
        "error": {
            "code": "NOT_FOUND",
            "message": f"Course with id {course_id} does not exist",
            "field": None
        }
    }
)

    if course.name is not None:
        existing_course.name = course.name

    if course.description is not None:
        existing_course.description = course.description

    if course.department_id is not None:
        existing_course.department_id = course.department_id

    await db.commit()
    await db.refresh(existing_course)

    return existing_course
@app.get(
    "/api/v1/courses/",
    tags=["Courses"]
)
async def get_courses(
    request: Request,
    page: int = 1,
    page_size: int = 2,
    search: str = "",
    db: AsyncSession = Depends(get_db)
):
    offset = (page - 1) * page_size

    query = select(Course)

    # Search by course name or description
    if search:
        query = query.where(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.description.ilike(f"%{search}%")
            )
        )

    # Total count
    total_result = await db.execute(
        select(func.count()).select_from(query.subquery())
    )
    total = total_result.scalar()

    # Paginated results
    result = await db.execute(
        query.offset(offset).limit(page_size)
    )

    courses = result.scalars().all()

    next_url = None
    if offset + page_size < total:
        next_url = str(
            request.url.include_query_params(
                page=page + 1,
                page_size=page_size,
                search=search
            )
        )

    previous_url = None
    if page > 1:
        previous_url = str(
            request.url.include_query_params(
                page=page - 1,
                page_size=page_size,
                search=search
            )
        )

    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": courses
    }
@app.post(
    "/api/v1/auth/register/",
    response_model=UserResponse,
    status_code=201
)
async def register_user(
    user: UserRegister,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(User.email == user.email)
    )

    existing = result.scalar_one_or_none()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    # bcrypt is intentionally slow and much safer than
    # MD5 or SHA-256 for storing passwords.

    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_active=1
    )

    db.add(new_user)

    await db.commit()

    await db.refresh(new_user)

    return new_user