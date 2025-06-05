from enum import Enum
from sqlalchemy import Column, Float, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class HangStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    DECLINED = "declined"

class Hang(Base):
    __tablename__ = "hang"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(Enum(HangStatus))
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="hangs")
    hang_start_time = Column(DateTime)
    hang_end_time = Column(DateTime)
    proposed_start_time = Column(DateTime)
    proposed_end_time = Column(DateTime)
    location_id = Column(Integer, ForeignKey("location.id"))
    created_by_user_id = Column(Integer, ForeignKey("user.id"))
    created_by_user = relationship("User", back_populates="hangs")
    participants = relationship("User", secondary="hang_participant", back_populates="hangs")
    location = relationship("Location", back_populates="hangs")


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
    location_id = Column(Integer, ForeignKey("location.id"))
    created_by_user_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

class Poll(Base):
    __tablename__ = "poll"

    id = Column(Integer, primary_key=True, index=True)
    hang_id = Column(Integer, ForeignKey("hang.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    location_id = Column(Integer, ForeignKey("location.id"))
    created_by_user_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PollOption(Base):
    __tablename__ = "poll_option"

    id = Column(Integer, primary_key=True, index=True)
    poll_id = Column(Integer, ForeignKey("poll.id"))
    option = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PollVote(Base):
    __tablename__ = "poll_vote"

    id = Column(Integer, primary_key=True, index=True)
    poll_id = Column(Integer, ForeignKey("poll.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    option_id = Column(Integer, ForeignKey("poll_option.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Availability(Base):
    __tablename__ = "availability"

    id = Column(Integer, primary_key=True, index=True)
    hang_id = Column(Integer, ForeignKey("hang.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

