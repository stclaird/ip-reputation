import datetime
from ipaddress import ip_address
from typing import Optional
from aredis_om.connections import get_redis_connection
from aredis_om.model import Field, HashModel, NotFoundError

from config import Redis

class Ip(HashModel):
    ip_address: str = Field(index=True)
    list_name: str  #The list this IP address was found on
    added_date: datetime.date #The date this was added
    ASN: Optional[str] #The BGP ASN number this address is part of

    class Meta:
        database = get_redis_connection(url=Redis.URL, decode_responses=True)
