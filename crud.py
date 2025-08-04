from sqlalchemy.orm import Session
import models, schemas

def get_parts(db: Session, search: str=""):
    return db.query(models.AutoPart).filter(models.AutoPart.name == search).all()

def create_part(db: Session, part: schemas.AutoPartCreate):
    db_part = models.AutoPart(name=part.name, description=part.description)
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

def delete_part(db: Session, part_id: int):
    db_part = db.query(models.AutoPart).filter(models.AutoPart.id == part_id).first()
    if db_part:
        db.delete(db_part)
        db.commit()
        return True
    return False