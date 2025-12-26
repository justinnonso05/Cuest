from pydantic import BaseModel, EmailStr, Field, UUID4
from datetime import datetime
from typing import Optional
from app.api.v1.auth.model import UserRole

# ============ Request Schemas ============

class UserRegister(BaseModel):
    """Schema for user registration"""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=2, max_length=100)
    password: str = Field(..., min_length=8, max_length=100)
    role: UserRole = UserRole.PARTICIPANT

class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    """Schema for token response"""
    access_token: str
    token_type: str = "bearer"
    user: "UserRead"

class PasswordChange(BaseModel):
    """Schema for password change"""
    old_password: str
    new_password: str = Field(..., min_length=8, max_length=100)

class ProfileUpdate(BaseModel):
    """Schema for profile update"""
    full_name: Optional[str] = Field(None, min_length=2, max_length=100)
    avatar_url: Optional[str] = None

# ============ Response Schemas ============

class UserRead(BaseModel):
    """Schema for user response"""
    id: UUID4
    email: EmailStr
    username: str
    full_name: str
    role: UserRole
    is_active: bool
    avatar_url: Optional[str] = None
    points: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserProfile(UserRead):
    """Extended user profile with additional details"""
    updated_at: datetime

    class Config:
        from_attributes = True

# Update forward references
TokenResponse.model_rebuild()
