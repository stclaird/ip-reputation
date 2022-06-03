from typing import Optional
import uuid
import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, validator


class IPModel(BaseModel):
    ip_address: str = Field(index=True)
    list_name: str  #The list this IP address was found on
    ASN: Optional[str] #The BGP ASN number this address is part of.
  
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "ip_addr":         "190.45.67.89",
                "list_name":       "https://lists.blocklist.de/lists/all.txt"
            }
        }

