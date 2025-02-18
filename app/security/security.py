from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.config import JWT_SECRET_KEY

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # print(JWT_SECRET_KEY)
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    # print(encoded_jwt)
    return encoded_jwt

def verify_token(token: str):
    try:
        # print(JWT_SECRET_KEY)
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        # print(payload)
        return payload
    except JWTError:
        # print(JWTError)
        return None

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    # print(payload)
    if payload is None:
         print(HTTPException(
             status_code=status.HTTP_401_UNAUTHORIZED,
             detail="Invalid authentication credentials",
             headers={"WWW-Authenticate": "Bearer"},
         ))
    return payload

# if __name__ == '__main__':
#     temp = get_current_user("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzM5ODM2NTc5fQ.YZJECHWgny7Cxhx5ANW85ry4gz1IfMur5ChDlsAw9vI")
#     print(temp)