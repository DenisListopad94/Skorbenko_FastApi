from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.auth.routers.user_router import router as user_router

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "age": 25, "email": "john.doe@example.com"},
    {"id": 2, "first_name": "Alice", "last_name": "Smith", "age": 30, "email": "alice.smith@example.com"},
    # Add more users here
]


@app.get("/users", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
