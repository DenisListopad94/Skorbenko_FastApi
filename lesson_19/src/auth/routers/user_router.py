from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from src.auth.schemas.user_schema import User
import re

router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)

# router.mount("/static", StaticFiles(directory="static"), name="users")
router.mount("/static", StaticFiles(directory="static"), name="users")
templates = Jinja2Templates(directory="templates")


@router.post("/")
def data_actor_validated(user: User) -> User:
    return user


def is_alphanumeric(text):
    return re.search(r"^[a-zA-Z]", text) is not None


@router.get("/get_template", response_class=HTMLResponse)
def get_users(request: Request):
    users = [
        {"id": 1, "first_name": "John", "last_name": "Doe", "age": 25, "email": "john.doe@example.com"},
        {"id": 2, "first_name": "Alice", "last_name": "Smith", "age": 30, "email": "alice.smith@example.com"},
    ]

    for user in users:
        user["is_alphanumeric"] = is_alphanumeric(user["name"])
        if user["is_alphanumeric"]:
            print(user)

    return templates.TemplateResponse(
        request=request,
        name="users.html",
        context={"data": users, "is_alphanumeric": is_alphanumeric}
    )
