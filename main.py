from fastapi import FastAPI,Depends
from models import product
from database import session,engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello"

products=[
    product(id=1,name="Mobile",description="A smartphone",price=900,quantity=3),
    product(id=2,name="Laptop",description="New gel pc",price=1900,quantity=13),
    product(id=3,name="Pencil",description="Sharp pencil",price=19,quantity=39),
    product(id=4,name="Watch",description="Know your valuable time",price=100,quantity=30),
    ]

def get_db():
    db = session()
    try:
        yield db    #yield="Pause here. After work is finished, continue and clean up.""Take this db for now… I will wait… after you're done, I will close it."
    finally:
        db.close()


def init_db():
    db= session() 

    count = db.query(database_models.Product).count      
   
    # If Product table is empty, insert initial default products
    # Prevents duplicate data on every app restart
    
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump())) #**->unpacking(and this will give you key,value pait),model_dump() give you a dict form object
    
        db.commit()
init_db() 

@app.get("/products") 
def all_products(db:Session=Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):
        db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
        if db_product:
            return db_product
        return "Invalid ID"

@app.post("/product")
def add_product(product: product, db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id:int,product:product, db:Session = Depends(get_db)):
        db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() 
        if db_product:
             db_product.name = product.name
             db_product.description = product.description
             db_product.price = product.price
             db_product.quantity = product.quantity
             db.commit() 
             return "Updated Successfully"
        else:
            return "invalid ID"



@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
         if products[i].id == id:
             del products[i]
             return "ID deleted"
    return "Invalid ID"
   



