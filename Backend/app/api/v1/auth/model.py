from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum
import uuid

class UserRole(str, enum.Enum):
    """User roles for the platform"""
    SUPER_ADMIN = "super_admin"
    PROJECT_OWNER = "project_owner"
    PARTICIPANT = "participant"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Role-based access
    role = Column(SQLEnum(UserRole), default=UserRole.PARTICIPANT, nullable=False)
    
    # Account status
    is_active = Column(Boolean, default=True)
    
    # Profile information
    avatar_url = Column(String, nullable=True)  # Profile picture URL
    
    # Points and rewards (for participants)
    points = Column(Integer, default=0)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships (will be added later)
    # surveys = relationship("Survey", back_populates="owner")
    # responses = relationship("Response", back_populates="participant")
