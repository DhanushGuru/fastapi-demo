class product():
    id: int
    Name: str
    description: str
    price: int
    quantity: int

    def __init__(self,id,Name,description,price,quantity):
        self.id = id
        self.Name= Name
        self.description = description
        self.price = price
        self.quantity = quantity