from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from starlette.requests import Request
from starlette.responses import Response

import aioredis

from typing import List
from config import General, Redis
from aredis_om.model import HashModel, NotFoundError
from model.ip import Ip
import json

router = APIRouter()

@router.get("/", tags=['Info'], include_in_schema = False)
async def root():
    return {
        "message": "root"
        }

@router.get("/health", tags=['Info'])
async def health():
    return {"status": "OK"}

@router.get("/info", tags=['Info'], include_in_schema = False)
async def info():
    return {
        "ENV": General.ENV,
        "SERVER_ENVIRONMENT" : General.SERVER_ENVIRONMENT,
        "VERSION" : General.VERSION
        }

@router.get("/ips")
async def list_customers(request: Request, response: Response):
    # To retrieve this customer with its primary key, we use `Customer.get()`:
    return {"ips": [pk async for pk in await Ip.all_pks()]}

@router.get("/ip/")
@cache(expire=10)
async def get_ip(pk: str, request: Request, response: Response):
    # To retrieve this customer with its primary key, we use `Customer.get()`:
    # try:
        # return await Ip.get(pk)
    return await Ip.find(Ip.ip_address == "1.11.62.187").all()
    # except NotFoundError:
    #     raise HTTPException(status_code=404, detail="IP Address not found")

@router.on_event("startup")
async def startup():
    r = aioredis.from_url(Redis.URL, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(r), prefix="fastapi-cache")