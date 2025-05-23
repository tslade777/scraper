from typing import List
from fastapi import APIRouter, Depends
from backend.dependencies import DBSession
from backend.models.bowling_balls import BowlingBall
from backend.database.equipment import *

router = APIRouter(prefix="/equipment", tags=["Equipment"])

@router.post("/balls", response_model=BowlingBall)
def add_ball(ball: BowlingBall, session: DBSession):
    return create_ball(session, ball)

@router.get("/balls", response_model=List[BowlingBall])
def get_balls(session: DBSession):
    return fetch_all_balls(session)

@router.get("/ball/{ball_ID}/", response_model=BowlingBall)
def get_ball(session: DBSession, ball_id: int):
    return fetch_ball(session, ball_id)
