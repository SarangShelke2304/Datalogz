from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Student, Course, Enrollment
from app.schemas import StudentCreate,CourseCreate,EnrollmentCreate

async def create_student(db: AsyncSession, student: StudentCreate):
    new_student = Student(**student.model_dump())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student

async def get_student_by_id(db: AsyncSession, student_id: int):
    return await db.get(Student, student_id)

async def create_course(db: AsyncSession, course: CourseCreate):
    new_course = Course(**course.model_dump())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course

async def get_course_by_id(db: AsyncSession, course_id: int):
    return await db.get(Course, course_id)

async def create_enrollment(db: AsyncSession, enrollment: EnrollmentCreate):
    new_enrollment = Enrollment(**enrollment.model_dump())
    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)
    return new_enrollment

async def get_enrolled_courses(db: AsyncSession, student_id: int):
    temp = select(Enrollment).where(Enrollment.student_id == student_id)
    result = await db.execute(temp)
    enrollments = result.scalars().all()
    course_id = [enrollments.course_id for enrollments in enrollments]
    return course_id