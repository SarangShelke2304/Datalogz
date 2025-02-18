from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import EnrollmentCreate, EnrollmentResponse, StudentCourses
from app.db.database import get_db
from app.crud import create_enrollment, get_enrolled_courses
from app.security.security import get_current_user

router = APIRouter()

@router.post("/enrollments", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
async def create_enrollment_endpoint(enrollment: EnrollmentCreate, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    await create_enrollment(db, enrollment)
    return EnrollmentResponse(message="Enrolled successfully")

@router.get("/student/{student_id}/courses", response_model=StudentCourses)
async def get_student_courses(student_id: int, db: AsyncSession = Depends(get_db)):
    courses = await get_enrolled_courses(db, student_id)
    if not courses:
        raise HTTPException(status_code=404, detail="No enrolled courses found")
    return StudentCourses(enrolled_courses=courses)