from fastapi import FastAPI
from models import product

app = FastAPI()
@app.get("/")
def greet():
    return "Hello"

products=[
    product(1,"Bottle","careful product",200,3),
    product(1,"pro2","cdes",10,2)]

@app.get("/products")
def all_products():
    return products