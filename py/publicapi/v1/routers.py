from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .models import IPModel

ip_router = APIRouter()

@ip_router.post("/", response_description="Add new IP")
async def create_location(request: Request, ip: IPModel = Body(...)):
    ip = jsonable_encoder(ip)
    new_ip = await request.app.mongodb["col_ips"].insert_one(ip)
    created_ip = await request.app.mongodb["col_ips"].find_one(
        {"_id": new_ip.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_ip)

"""Get all IP Addresses"""
@ip_router.get("/", response_description="Get all IPs")
async def list_ips(request: Request):

    ips = []
    for doc in await request.app.mongodb["col_ips"].find().to_list(length=100):
        ips.append(doc)
    return ips

"""Get IP Address"""
@ip_router.get("/{id}", response_description="Get a single IP")
async def show_ip(id: str, request: Request):
    if (location := await request.app.mongodb["col_ips"].find_one({"_id": id})) is not None:
        return location

    raise HTTPException(status_code=404, detail=f"IP {id} not found")

"""Delete an IP address"""
@ip_router.delete("/{id}", response_description="Delete IP")
async def delete_ip(id: str, request: Request):
    delete_result = await request.app.mongodb["col_ips"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"IP {id} not found")
