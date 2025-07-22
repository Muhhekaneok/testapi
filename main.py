from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    quantity: int


items_db = []


@app.get("/")
def read_root():
    return {"message": "wtf, world?"}


@app.get("/items/")
def get_all_items():
    return {"message": "All items", "items": items_db}


@app.post("/items/")
def create_item(item: Item):
    items_db.append(item)
    return {"message": f"Item {item.name} created successfully.", "item": item}


@app.put("/items/{item_name}")
def update_item(item_name: str, updated_item: Item):
    for i, item in enumerate(items_db):
        if item.name == item_name:
            if updated_item.name != item_name:
                raise HTTPException(status_code=400, detail="Item name in URL and body must match")
            items_db[i] = updated_item
            return {"message": f"Item {item_name} updated successfully.", "item": updated_item}
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_name}")
def delete_item(item_name: str):
    for i, item in enumerate(items_db):
        if item.name == item_name:
            deleted_item = items_db.pop(i)
            return {"message": f"Item {item_name} deleted successfully.", "item:": deleted_item}
    raise HTTPException(status_code=404, detail=f"Item {item_name} not found for deletion")

