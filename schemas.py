import datetime as _dt
import pydantic as _pydantic

class _UserBase(_pydantic.BaseModel):
    email: str

class UserCreate(_UserBase):
    password: str

    class Config:
        orm_mode = True

class User(_UserBase):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True

class _PostBsae(_pydantic.BaseModel):
    post_text: str

class PostCreate(_PostBsae):
    pass

class Post(_PostBsae):
    id: int
    owner_id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True