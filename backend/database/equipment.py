import bcrypt
from sqlmodel import Session, select
from backend.database.schema import BowlingBall
from sqlmodel import Session, select
from backend.exceptions import CantRemoveChatOwner, EntityNotFound, Unauthorized, UnprocessableEntity
from fastapi.responses import JSONResponse


def create_ball(session: Session, ball: BowlingBall) -> BowlingBall:
    existing = session.exec(select(BowlingBall).where(BowlingBall.link == ball.link)).first()
    if existing:
        return existing  # or update if needed

    session.add(ball)
    session.commit()
    session.refresh(ball)
    return ball

def fetch_all_balls(session: Session):
    return session.exec(select(BowlingBall)).all()

def fetch_ball(session: Session, id:int):
    result = session.exec(select(BowlingBall).where(BowlingBall.id == id))
    return result.first()