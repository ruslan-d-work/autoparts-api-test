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

@app.put("/parts/{part_id}")
def update_part(part_id: int, updated_part: schemas.AutoPartUpdate, db: Session = Depends(get_db)):
    part = db.query(models.AutoPart).filter(models.AutoPart.id == part_id).first()
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")

    if updated_part.name is not None:
        part.name = updated_part.name
    if updated_part.description is not None:
        part.description = updated_part.description
    if updated_part.price is not None:
        part.price = updated_part.price

    db.commit()
    db.refresh(part)
    return part



