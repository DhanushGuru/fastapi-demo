from fastapi import FastAPI
from models import product
from database import session,engine
import database_models;


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
def all_products():
 
    return products 

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "Invalid ID"

@app.post("/product")
def add_product(product: product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id:int,product:product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product added successfully"
        return "invalid ID"



@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
         if products[i].id == id:
             del products[i]
             return "ID deleted"
    return "Invalid ID"
   



