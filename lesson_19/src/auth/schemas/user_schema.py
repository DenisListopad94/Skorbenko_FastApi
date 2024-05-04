from pydantic import BaseModel, EmailStr, PositiveInt, Field, constr
from typing_extensions import Literal


class User(BaseModel):
    user_id: PositiveInt
    name: constr(min_length=2, max_length=20)
    surname: constr(min_length=2, max_length=20)
    age: int = Field(ge=0, le=100)
    sex: Literal["male", "female"]
    email: EmailStr