"""Database table models."""

from datetime import datetime, timezone

from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
from datetime import date

class BowlingBall(SQLModel, table=True):
    __tablename__ = "bowling_balls"  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)
    
    title: str
    link: str
    brand: Optional[str] = None
    core: Optional[str] = None
    coverstock: Optional[str] = None
    scent: Optional[str] = None
    release_date: Optional[date] = None
    image_url: Optional[str] = None
    rg: Optional[float] = None               # Radius of Gyration
    diff: Optional[float] = None             # Differential
    mass_bias: Optional[float] = None        # Intermediate Differential (if asymmetric)
    upload_date: date = Field(default_factory=datetime.now(timezone.utc))
    last_updated: Optional[date] = Field(default_factory=datetime.now(timezone.utc))
    original_price: Optional[str] = None
    discounted_price: Optional[str] = None