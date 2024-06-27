from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from fastapi import FastAPI, Depends, HTTPException, Path
import schemas
from schemas import ItemRequest, ItemCreate, ItemWithID
import models
from models import Items
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Provide a session for each endpoint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/items', status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Items).all()

# Retrieving an Item by ID
@app.get('/items/{id}', response_model=schemas.ItemWithID, status_code=status.HTTP_200_OK)
async def get_item(db: db_dependency, id: int):
    db_item = db.query(models.Items).filter(models.Items.id == id).first()
    if db_item is not None:
        return db_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')

# Creating a new Item
@app.post('/items', response_model=schemas.ItemWithID, status_code=status.HTTP_201_CREATED)
async def create_item(db: db_dependency, item: ItemCreate):
    db_item = models.Items(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Updating an Item
@app.put('/items/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_item(db: db_dependency, item: ItemRequest, id: int):
    db_item = db.query(Items).filter(models.Items.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    
    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price
    db_item.tax = item.tax
    
    db.commit()
    db.refresh(db_item)
    return db_item

# Deleting an Item
@app.delete('/items/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(db: db_dependency, id: int):
    db_item = db.query(Items).filter(models.Items.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
    
    db.delete(db_item)
    db.commit()
    return {"message": f"id: {id} has been deleted"}

# Delete all
@app.delete('/items', status_code=status.HTTP_200_OK)
async def delete_all(db: db_dependency):
    db.query(Items).delete()
    db.commit()
    return {"message": "All items have been deleted"}
