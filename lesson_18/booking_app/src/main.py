import random
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, validators, PositiveInt, Field, constr
from typing_extensions import Literal


class Actor(BaseModel):
    actor_id: int
    name: str
    surname: str
    age: int
    sex: str
    email: EmailStr


app = FastAPI()


@app.get("/random_numbers")
def get_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(5)]
    return numbers


@app.get("/item/{item_id}")
def get_item_by_id(item_id: int):
    return {"item_id": item_id}


@app.get("/query_params")
def get_query_params(int_param: int, str_param: str):
    return {"int_param": int_param, "str_param": str_param}


@app.get("/combined_params/{str_param}")
def get_combined_params(str_param: str, int_param1: int, int_param2: int):
    return {"str_param": str_param, "int_param1": int_param1, "int_param2": int_param2}


@app.post("/actors/")
def create_actor(actor: Actor):
    return actor


class ActorVal(BaseModel):
    actor_id: PositiveInt
    name: constr(min_length=2, max_length=20)
    surname: constr(min_length=2, max_length=20)
    age: int = Field(ge=0, le=100)
    sex: Literal["male", "female"]
    email: EmailStr


@app.post("/{actors_val}")
def data_actor_validated(actor_val: ActorVal):
    return actor_val