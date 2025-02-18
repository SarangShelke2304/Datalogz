from fastapi import APIRouter, status, HTTPException, Depends
from app.crud import get_course_by_id, create_course
from app.db.database import get_db
from app.schemas import Course, CourseCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.security.security import get_current_user

router = APIRouter()

@router.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
async def create_course_endpoint(course: CourseCreate, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    new_course = await create_course(db, course)
    return new_course

@router.get("/courses/{course_id}", response_model=Course)
async def get_course_endpoint(course_id: int, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    course = await get_course_by_id(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course