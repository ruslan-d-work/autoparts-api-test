from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, models, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

#dependecies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/parts/", response_model=list[schemas.AutoPart])
def read_parts(
    search: str = "",
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_parts(db=db, search=search)

@app.delete("/parts/{part_id}")
def delete_part(part_id: int, db: Session = Depends(get_db)):
    success = crud.delete_part(db=db, part_id=part_id)
    if not success:
        raise HTTPException(status_code=404, detail="Part not found")
    return {"success": 'Deleted'}

@app.post("/parts/", response_model=schemas.AutoPart)
def create_part(part: schemas.AutoPartCreate, db: Session = Depends(get_db)):
    return crud.create_part(db=db, part=part)


