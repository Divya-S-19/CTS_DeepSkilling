from pydantic import BaseModel
from typing import Optional
from pydantic import EmailStr

class UserRegister(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: int

    class Config:
        from_attributes = True
        
class CourseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    department_id: Optional[int] = None


# -------------------
# Course Schemas
# -------------------

class CourseCreate(BaseModel):
    name: str
    description: str
    department_id: int


class CourseResponse(CourseCreate):
    id: int

    class Config:
        from_attributes = True



# -------------------
# Student Schemas
# -------------------

class StudentCreate(BaseModel):
    name: str
    email: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True



# -------------------
# Enrollment Schemas
# -------------------

class EnrollmentCreate(BaseModel):
    course_id: int
    student_id: int


class EnrollmentResponse(EnrollmentCreate):
    id: int

    class Config:
        from_attributes = True