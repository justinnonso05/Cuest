# Cuest Backend API

FastAPI backend for the Cuest project with modular architecture.

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
- Update `.env` file with your configuration

4. Run the application:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
Backend/
├── app/
│   ├── api/
│   │   └── v1/                    # API Version 1
│   │       ├── users/             # Users Module
│   │       │   ├── __init__.py
│   │       │   ├── model.py       # User database model
│   │       │   ├── schema.py      # User Pydantic schemas
│   │       │   ├── service.py     # User business logic
│   │       │   └── router.py      # User API endpoints
│   │       ├── items/             # Items Module
│   │       │   ├── __init__.py
│   │       │   ├── model.py       # Item database model
│   │       │   ├── schema.py      # Item Pydantic schemas
│   │       │   ├── service.py     # Item business logic
│   │       │   └── router.py      # Item API endpoints
│   │       └── router.py          # Main v1 router
│   ├── database.py                # Database configuration
│   └── __init__.py
├── main.py                        # Application entry point
├── requirements.txt               # Dependencies
├── .env                           # Environment variables
└── .gitignore                     # Git ignore file
```

## Modular Architecture

Each module (users, items, etc.) is self-contained with:
- **model.py**: SQLAlchemy database model
- **schema.py**: Pydantic schemas for validation
- **service.py**: Business logic layer
- **router.py**: API endpoints

This structure makes it easy to:
- Add new modules
- Maintain code independently
- Scale the application
- Version the API

## Available Endpoints

### Users (v1)
- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/` - List users
- `GET /api/v1/users/{id}` - Get user
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

### Items (v1)
- `POST /api/v1/items/` - Create item
- `GET /api/v1/items/` - List items
- `GET /api/v1/items/{id}` - Get item
- `PUT /api/v1/items/{id}` - Update item
- `DELETE /api/v1/items/{id}` - Delete item

## Adding New Modules

To add a new module (e.g., "products"):

1. Create folder: `app/api/v1/products/`
2. Add files:
   - `__init__.py`
   - `model.py` (database model)
   - `schema.py` (Pydantic schemas)
   - `service.py` (business logic)
   - `router.py` (API endpoints)
3. Import in `app/api/v1/router.py`
4. Include router in the main API router

## Future Versions

To add v2:
1. Create `app/api/v2/` directory
2. Copy and modify modules as needed
3. Create `app/api/v2/router.py`
4. Include in `main.py` with prefix `/api/v2`
