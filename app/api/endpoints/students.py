from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas import Student, StudentCreate
from app.crud import create_student, get_student_by_id
from app.security.security import get_current_user

router = APIRouter()

@router.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student_endpoint(student: StudentCreate, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    new_student = await create_student(db, student)
    return new_student

@router.get("/students/{student_id}", response_model=Student)
async def get_student_endpoint(student_id: int, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    student = await get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student