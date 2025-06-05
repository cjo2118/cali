from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class Hang(Base):
    __tablename__ = "hang"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="hangs")


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Friend(Base):
    __tablename__ = "friend"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    friend_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class FriendGroup(Base):
    __tablename__ = "friend_group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class FriendGroupMember(Base):
    __tablename__ = "friend_group_member"

    id = Column(Integer, primary_key=True, index=True)
    friend_group_id = Column(Integer, ForeignKey("friend_groups.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class FavoriteType(Enum):
    INDIVIDUAL = "individual"
    GROUP = "group"

class FavoriteStatus(Enum):
    TRIED = "tried"
    NOT_TRIED = "not_tried"

class Favorite(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(FavoriteType))
    status = Column(Enum(FavoriteStatus))
    user_id = Column(Integer, ForeignKey("user.id"))
    hang_id = Column(Integer, ForeignKey("hang.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    created_by_user_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)