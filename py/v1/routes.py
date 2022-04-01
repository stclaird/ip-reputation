from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from config import General
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
