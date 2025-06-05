from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import plans, groups
from database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(plans.router, prefix="/api/v1", tags=["plans"])
app.include_router(groups.router, prefix="/api/v1", tags=["groups"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"} 