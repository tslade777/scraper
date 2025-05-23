from sqlmodel import Session, select
from backend.database.schema import BowlingBall
from backend.dependencies import engine  # where your DB connection is defined
from dateutil.parser import parse
from datetime import date

def _to_date(value):
    try:
        return parse(value).date()
    except Exception:
        return None

def save_bowling_ball(ball_data: dict):
    title = ball_data.get("title") or ball_data.get("Title")
    brand = ball_data.get("brand") or ball_data.get("Brand")

    if not title:
        print("❌ Skipping: missing required title")
        return

    # Normalize keys to match schema
    normalized_data = {
        "title": title,
        "link": ball_data.get("link") or ball_data.get("Link"),
        "brand": brand,
        "core": ball_data.get("core"),
        "coverstock": ball_data.get("coverstock"),
        "scent": ball_data.get("scent"),
       "release_date": _to_date(ball_data.get("release_date")),
        "image_url": ball_data.get("image_url") or ball_data.get("Image URL"),
        "rg": _to_float(ball_data.get("rg")),
        "diff": _to_float(ball_data.get("diff")),
        "mass_bias": _to_float(ball_data.get("mass_bias")),
        "original_price": ball_data.get("original_price"),
        "discounted_price": ball_data.get("discounted_price"),
        "color" : ball_data.get("color"),
        "finish" : ball_data.get("finish"),
        "flare" : ball_data.get("flare")
    }

    with Session(engine) as session:
        existing = session.exec(
            select(BowlingBall).where(BowlingBall.link == normalized_data["link"])
        ).first()

        if existing:
            for key, value in normalized_data.items():
                setattr(existing, key, value)
            session.add(existing)
        else:
            ball = BowlingBall(**normalized_data)
            session.add(ball)

        session.commit()

def _to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

