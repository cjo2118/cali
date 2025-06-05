# FastAPI Backend

This is a FastAPI backend application with PostgreSQL database integration.

## Project Structure
```
backend/
├── README.md
├── requirements.txt
├── main.py
├── database.py
├── models.py
├── schemas.py
└── routers/
    ├── __init__.py
    ├── plans.py
    └── groups.py
```

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## API Documentation

Once the application is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints

- GET /api/v1/plans/ - List all plans
- GET /api/v1/groups/ - List all groups
- POST /api/v1/groups/ - Create a new group 