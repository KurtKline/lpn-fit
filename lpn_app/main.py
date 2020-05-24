from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/points/", response_model=List[schemas.PointEvent])
def read_point_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    point_logs = crud.get_point_logs(db, skip=skip, limit=limit)
    return point_logs


@app.get("/points/player/{player}", response_model=List[schemas.PointEvent])
def read_player(player: str, db: Session = Depends(get_db)):
    db_player = crud.get_points_by_player(db, player=player)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


@app.get("/points/team/{team}", response_model=List[schemas.PointEvent])
def read_team(team: str, db: Session = Depends(get_db)):
    db_team = crud.get_points_by_team(db, team=team)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team


@app.get("/points/season/{season}", response_model=List[schemas.PointEvent])
def read_season(season: str, db: Session = Depends(get_db)):
    db_season = crud.get_points_by_season(db, season=season)
    if db_season is None:
        raise HTTPException(status_code=404, detail="Season not found")
    return db_season


@app.get("/points/team/{team}/season/{season}", response_model=List[schemas.PointEvent])
def read_team_and_season(team: str, season: str, db: Session = Depends(get_db)):
    db_ts = crud.get_points_by_team_and_season(db, team=team, season=season)
    if db_ts is None:
        raise HTTPException(
            status_code=404, detail="Team and Season combination not found"
        )
    return db_ts


@app.get(
    "/points/player/{player}/season/{season}", response_model=List[schemas.PointEvent]
)
def read_player_and_season(player: str, season: str, db: Session = Depends(get_db)):
    db_ps = crud.get_points_by_player_and_season(db, player=player, season=season)
    if db_ps is None:
        raise HTTPException(
            status_code=404, detail="Player and Season combination not found"
        )
    return db_ps
