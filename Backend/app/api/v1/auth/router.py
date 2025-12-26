from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.api.v1.auth.schema import (
    UserRegister, UserLogin, TokenResponse, UserRead, 
    UserProfile, PasswordChange, ProfileUpdate
)
from app.api.v1.auth.service import AuthService, get_current_user, require_role
from app.api.v1.auth.model import User, UserRole

router = APIRouter()

# ============ Public Endpoints ============

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """
    Register a new user
    
    - **email**: Valid email address
    - **username**: Unique username (3-50 characters)
    - **full_name**: Full name (2-100 characters)
    - **password**: Strong password (min 8 characters)
    - **role**: User role (participant, project_owner, super_admin)
    """
    service = AuthService(db)
    return service.register_user(user_data)


@router.post("/login", response_model=TokenResponse)
async def login(login_data: UserLogin, db: Session = Depends(get_db)):
    """
    Login and get access token
    
    - **email**: Registered email address
    - **password**: User password
    
    Returns JWT access token and user information
    """
    service = AuthService(db)
    user = service.authenticate_user(login_data)
    access_token = service.create_access_token(user.id, user.role.value)
    
    return TokenResponse(
        access_token=access_token,
        user=UserRead.model_validate(user)
    )


# ============ Protected Endpoints ============

@router.get("/me", response_model=UserProfile)
async def get_current_user_profile(current_user: User = Depends(get_current_user)):
    """
    Get current user profile
    
    Requires authentication
    """
    return UserProfile.model_validate(current_user)


@router.put("/me", response_model=UserProfile)
async def update_current_user_profile(
    profile_data: ProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update current user profile
    
    Requires authentication
    """
    service = AuthService(db)
    updated_user = service.update_profile(current_user.id, profile_data)
    return UserProfile.model_validate(updated_user)


@router.post("/change-password", status_code=status.HTTP_200_OK)
async def change_password(
    password_data: PasswordChange,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Change user password
    
    Requires authentication
    """
    service = AuthService(db)
    service.change_password(current_user.id, password_data)
    return {"message": "Password changed successfully"}


# ============ Admin Endpoints ============

@router.get("/users", response_model=List[UserRead])
async def list_all_users(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(require_role([UserRole.SUPER_ADMIN])),
    db: Session = Depends(get_db)
):
    """
    List all users (Admin only)
    
    Requires SUPER_ADMIN role
    """
    users = db.query(User).offset(skip).limit(limit).all()
    return [UserRead.model_validate(user) for user in users]


@router.get("/users/{user_id}", response_model=UserProfile)
async def get_user_by_id(
    user_id: str,
    current_user: User = Depends(require_role([UserRole.SUPER_ADMIN])),
    db: Session = Depends(get_db)
):
    """
    Get user by ID (Admin only)
    
    Requires SUPER_ADMIN role
    """
    service = AuthService(db)
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return UserProfile.model_validate(user)


@router.patch("/users/{user_id}/toggle-active", response_model=UserRead)
async def toggle_user_active_status(
    user_id: str,
    current_user: User = Depends(require_role([UserRole.SUPER_ADMIN])),
    db: Session = Depends(get_db)
):
    """
    Toggle user active status (Admin only)
    
    Requires SUPER_ADMIN role
    """
    service = AuthService(db)
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user.is_active = not user.is_active
    db.commit()
    db.refresh(user)
    return UserRead.model_validate(user)
