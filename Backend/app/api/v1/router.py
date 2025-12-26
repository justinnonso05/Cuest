from fastapi import APIRouter
from app.api.v1.auth.router import router as auth_router
    
api_router = APIRouter()

# Include all module routers
api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
