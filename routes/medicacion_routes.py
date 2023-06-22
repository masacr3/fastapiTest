from fastapi import APIRouter
from models.medicacion_model import Medicacion
from schemas.medicacion_schema import medicaciones_serializer
from bson import ObjectId
from config.db import collection

medicacion = APIRouter()

@medicacion.post("/medicacion")
async def create_medicacion( medicacion: Medicacion):
    _id = collection.insert_one(dict(medicacion))
    medicacion = medicaciones_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok", "data": medicacion}

@medicacion.put("/medicacion/{id}")
async def update_medicacion( id : str, medicacion: Medicacion):
    query = {"_id" : ObjectId(id)}
    update = { "$set" : dict(medicacion) } 
    collection.find_one_and_update(query, update)
    medicacion = medicaciones_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": medicacion}


@medicacion.delete("/medicacion/{id}")
async def eliminar_medicacion( id : str):
    query = { "_id" : ObjectId(id)}
    collection.find_one_and_delete(query)
    return {"status": "Ok", "data" : []}

@medicacion.get("/medicacion")
async def find_all_medicacion():
    medicaciones = medicaciones_serializer(collection.find())
    return {"status": "Ok", "data": medicaciones}

