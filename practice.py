from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel  #Used in def create_item method for class item

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    category: Optional[str] = None  #Can make a default value instead of None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None

inventory = {
    1: {
        "name": "Tea",
        "price": 2.99,
        "category": "Beverage"
        },
    2: {
        "name": "Ice Cream",
        "price": 5.99,
        "category": "Dessert"
        }
}

class Item(BaseModel):
    name: str
    price: float
    category: Optional[str]

#4 core HTTP requests/methods: get, post, put, delete
#in terminal: python3 -m uvicorn practice:app --reload
    #Must reload from the same location of the "working" (i.e. pratice) file
    #See on browser at 

@app.get("/")
def home():
    return "Restaurant Menu"

@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item")):
    return inventory[item_id]

@app.get("/get_item_by_name")
def get_item(name: str = Query(None, title="Name", description="The name of the item")):
    for item_id in inventory:
        #if inventory[item_id]["name"] == name:     --> no BaseModel
        if inventory[item_id].name == name:         #-> With BaseModel
            return inventory[item_id]
    return {"Data": "Not Found"}
    #raise HTTPException(status_code=404) OR
    #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    #raise HTTPException(status_code=404, detail = "Item name not found")       Do not need to return error message if raise HTTPException

@app.post("/create_item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"ERROR: This ID already exists."}
    #inventory[item_id] = {"name" = item.name, "price" = item.price, "category" = item.category}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update_item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"ERROR: This ID does not exist."}
    #inventory[item_id] = item
    #OR
    #inventory[item_id].update(UpdateItem)       #Must create new class (UpdateItem) otherwise will need to re-enter all data???
        #This doesn't work since it is not a python dictionary? (it is an instance of an object item class, not python dictionary)

    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.category != None:
        inventory[item_id].category = item.category
    return inventory[item_id]

#2 different ways to delete item
@app.delete("/delete_item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete")):     #... means required field       This method has embedded "Quer
    if item_id not in inventory:
        return {"ERROR: ID of item does not exist."}
    del inventory[item_id]
    return {"Success! Item has been deleted."}

@app.delete("/delete_item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        return {"ERROR: ID does not exist."}
    del inventory[item_id]
    return {"Success! Item has been deleted."}

    