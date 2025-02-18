from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    name: str
    age: int
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int


class CourseBase(BaseModel):
    title: str
    description: str = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentResponse(BaseModel):
    message: str

class StudentCourses(BaseModel):
    enrolled_courses: list[int]
