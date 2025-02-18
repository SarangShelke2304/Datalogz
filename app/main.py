from fastapi import FastAPI
from app.api.endpoints import students, courses, enrollments, auth
from pathlib import Path

desc = Path("api_docs.md").read_text()
# print(desc)

app = FastAPI(
    title="API docs",
    description=desc,
    version="1.0.0",
    openapi_url="/openapi.json"
)
app.include_router(auth.router, tags=["auth"])
app.include_router(students.router, tags=["students"])
app.include_router(courses.router, tags=["courses"])
app.include_router(enrollments.router, tags=["enrollments"])

app.get("/")
@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to the Student's Management System!"}
