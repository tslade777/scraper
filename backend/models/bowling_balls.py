from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class BowlingBall(BaseModel):
    id: Optional[int]
    title: str
    link: str
    brand: Optional[str]
    core: Optional[str]
    coverstock: Optional[str]
    scent: Optional[str]
    release_date: Optional[date]
    image_url: str
    rg: Optional[float] = None               # Radius of Gyration
    diff: Optional[float] = None             # Differential
    mass_bias: Optional[float] = None        # Intermediate Differential (if asymmetric)
    upload_date: date
    last_updated: Optional[date]
    original_price: Optional[str] = None
    discounted_price: Optional[str] = None
    color : Optional[str] = None
    finish : Optional[str] = None
    flare : Optional[str] = None

    