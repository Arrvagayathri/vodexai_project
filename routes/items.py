from fastapi import APIRouter, HTTPException
from bson import ObjectId
from database import items_collection
from models import Item, UpdateItem
from datetime import date, datetime


router = APIRouter()

@router.post("/items", response_description="Add new item")
async def create_item(item: Item):
    item_data = item.dict()

    if 'expiry_date' in item_data:
        item_data["expiry_date"] = datetime.combine(item_data["expiry_date"], datetime.min.time())

    item_data["insert_date"] = datetime.now()
    new_item = items_collection.insert_one(item_data)
    return {"id": str(new_item.inserted_id)}

def convert_objectid(item):
    if "_id" in item:
        item["_id"] = str(item["_id"])
    return item

@router.get("/items/filter_by")
async def filter_items(email: str = None, expiry_date: date = None, insert_date: date = None, quantity: int = None):
    query = {}
    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gt": expiry_date}
    if insert_date:
        query["insert_date"] = {"$gt": datetime.combine(insert_date, datetime.min.time())}
    if quantity:
        query["quantity"] = {"$gte": quantity}
    items = list(items_collection.find(query))
    for item in items:
        item = convert_objectid(item)
    
    return items

@router.get("/items/aggregate")
async def aggregate_items():
    pipeline = [
        {"$group": {"_id": "$email", "total_items": {"$sum": 1}}}
    ]
    result = list(items_collection.aggregate(pipeline))
    return result

@router.get("/items/{id}")
async def get_item(id: str):
    if (item := items_collection.find_one({"_id": ObjectId(id)})) is not None:
        
        item["_id"] = str(item["_id"])
    
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{id}")
async def update_item(id: str, update_data: UpdateItem):
    # Convert Pydantic model to dictionary and remove None values
    update_data = {k: v for k, v in update_data.dict().items() if v is not None}
    if 'expiry_date' in update_data:
        update_data["expiry_date"] = datetime.combine(update_data["expiry_date"], datetime.min.time())

    
    # Perform the update only if there are fields to update
    if update_data:
        result = items_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})

        if result.matched_count:
            return {"msg": "Item updated"}
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/items/{id}")
async def delete_item(id: str):
    result = items_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return {"msg": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
