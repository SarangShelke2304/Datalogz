from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import timedelta
from app.security.security import create_access_token

router = APIRouter()
security = HTTPBearer()

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/token")
async def login_for_access_token(login_request: LoginData):
    if login_request.username != "user" or login_request.password != "password":
         raise HTTPException(
             status_code=status.HTTP_401_UNAUTHORIZED,
             detail="Incorrect username or password",
             headers={"WWW-Authenticate": "Bearer"},
         )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": login_request.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
