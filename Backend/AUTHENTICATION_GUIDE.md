# Cuest Authentication System

## ✅ Completed Implementation

### **User Model with UUID**
- **ID**: UUID instead of integer for better security and scalability
- **Roles**: SUPER_ADMIN, PROJECT_OWNER, PARTICIPANT
- **Generic Fields**: 
  - `organization` (instead of department)
  - `bio` (user description)
  - `avatar_url` (profile picture)
  - Removed student-specific fields (matric_number, department)

### **Authentication Features**
1. **User Registration** (`POST /api/v1/auth/register`)
   - Email validation
   - Username uniqueness check
   - Password hashing with bcrypt
   - Role selection

2. **User Login** (`POST /api/v1/auth/login`)
   - JWT token generation
   - Last login tracking
   - Account status validation

3. **Profile Management** (`GET/PUT /api/v1/auth/me`)
   - View current user profile
   - Update profile information
   - Change password

4. **Admin Endpoints** (SUPER_ADMIN only)
   - List all users
   - View user by ID
   - Toggle user active status

### **Security Features**
- JWT-based authentication
- Password hashing with bcrypt 4.0.1
- Role-based access control
- HTTP Bearer token authentication

## 📝 Next Steps

### **1. Create Migration**
```bash
# Drop old tables and create new ones
alembic revision --autogenerate -m "Add UUID-based auth system"
alembic upgrade head
```

### **2. Test the API**
```bash
python main.py
```

Visit: http://localhost:8000/docs

### **3. Sample API Calls**

**Register a Participant:**
```json
POST /api/v1/auth/register
{
  "email": "student@ui.edu.ng",
  "username": "john_doe",
  "full_name": "John Doe",
  "password": "SecurePass123",
  "role": "participant",
  "organization": "University of Ibadan",
  "bio": "Final year student"
}
```

**Register a Project Owner:**
```json
POST /api/v1/auth/register
{
  "email": "researcher@ui.edu.ng",
  "username": "jane_researcher",
  "full_name": "Jane Researcher",
  "password": "SecurePass123",
  "role": "project_owner",
  "organization": "University of Ibadan",
  "bio": "Final year project on AI"
}
```

**Login:**
```json
POST /api/v1/auth/login
{
  "email": "student@ui.edu.ng",
  "password": "SecurePass123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "student@ui.edu.ng",
    "username": "john_doe",
    "full_name": "John Doe",
    "role": "participant",
    "is_active": true,
    "is_verified": false,
    "points": 0,
    ...
  }
}
```

**Get Profile (with token):**
```
GET /api/v1/auth/me
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

## 🏗️ Future Modules to Build

1. **Surveys Module**
   - Create/edit/delete surveys
   - Question types (multiple choice, text, rating, etc.)
   - Survey templates
   - QR code generation
   - WhatsApp sharing

2. **Responses Module**
   - Submit survey responses
   - Duplicate prevention
   - Anonymous responses
   - Response validation

3. **Rewards Module**
   - Points system
   - Badges
   - Leaderboards
   - Spin and win
   - Payout management

4. **Analytics Module**
   - Response statistics
   - Charts and visualizations
   - Data export (Excel, SPSS)
   - AI-powered insights

5. **Admin Module**
   - Survey approval/rejection
   - User management
   - Platform analytics
   - Fraud detection

## 📚 Project Structure

```
Backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth/              ✅ COMPLETED
│   │       │   ├── model.py       # User model with UUID
│   │       │   ├── schema.py      # Pydantic schemas
│   │       │   ├── service.py     # Auth logic
│   │       │   └── router.py      # API endpoints
│   │       ├── items/             # Example module (can be removed)
│   │       └── router.py          # Main v1 router
│   └── database.py
├── alembic/                       # Database migrations
├── main.py
├── requirements.txt
└── .env
```

## 🔐 Environment Variables

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/cuest
SECRET_KEY=O2av7lz50llMYDOYhr6ZxomnZzzbTaZQl_Jf8JZvNo8
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True
API_VERSION=v1
```

## 🎯 Ready to Build!

The authentication foundation is complete. You can now:
1. Run migrations to create the database
2. Test the authentication endpoints
3. Start building the Surveys module next!
