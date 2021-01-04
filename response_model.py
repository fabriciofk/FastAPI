from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None


class UserIn(UserBase):
    password: str


class UserOut(BaseModel):
    pass


class UserInDB(BaseModel):
    hashed_password: str


@app.post("/user/",
          response_model=UserIn,
          response_model_exclude_unset=True,
          response_model_exclude={'password'}
          )
async def create_user(user: UserIn):
    return user


def fake_password_hasher(raw_password: str):
    return 'supersecret' + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print('User saved! ..not really')
    return user_in_db


@app.post('useradd/', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved



