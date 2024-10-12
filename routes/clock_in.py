from fastapi import APIRouter, HTTPException
from bson import ObjectId
from database import clock_in_collection
from models import ClockIn, UpdateClockIn
from datetime import date, datetime


router = APIRouter()

@router.post("/clock-in")
async def create_clock_in(clock_in: ClockIn):
    clock_in_data = clock_in.dict()
    clock_in_data["insert_datetime"] = datetime.now()
    new_clock_in = clock_in_collection.insert_one(clock_in_data)
    return {"id": str(new_clock_in.inserted_id)}


def convert_objectid(item):
    if "_id" in item:
        item["_id"] = str(item["_id"])
    return item

@router.get("/clock-in/filter")
async def filter_clock_in(email: str = None, location: str = None, insert_datetime: datetime = None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gt": insert_datetime}
    records = list(clock_in_collection.find(query))
    for record in records:
        record = convert_objectid(record)
    
    return records

@router.get("/clock-in/{id}")
async def get_clock_in(id: str):
    if (record := clock_in_collection.find_one({"_id": ObjectId(id)})) is not None:
        record["_id"] = str(record["_id"])

        return record
    raise HTTPException(status_code=404, detail="Clock-in record not found")

@router.put("/clock-in/{id}")
async def update_clock_in(id: str, update_data: UpdateClockIn):
    update_data = {k: v for k, v in update_data.dict().items() if v is not None}
    if update_data:
        result = clock_in_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count:
            return {"msg": "Clock-in record updated"}
    raise HTTPException(status_code=404, detail="Clock-in record not found")

@router.delete("/clock-in/{id}")
async def delete_clock_in(id: str):
    result = clock_in_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return {"msg": "Clock-in record deleted"}
    raise HTTPException(status_code=404, detail="Clock-in record not found")
