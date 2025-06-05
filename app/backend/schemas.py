from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Plan schemas
class PlanBase(BaseModel):
    name: str
    description: Optional[str] = None

class PlanCreate(PlanBase):
    pass

class Plan(PlanBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Group schemas
class GroupBase(BaseModel):
    name: str
    description: Optional[str] = None

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 