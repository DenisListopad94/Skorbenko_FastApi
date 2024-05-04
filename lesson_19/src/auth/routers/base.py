import fastapi
from src.auth.routers.user_router import router as user_router

router = fastapi.APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(user_router)