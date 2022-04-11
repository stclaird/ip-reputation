import datetime
import asyncio
import aioredis

from ip import Ip


# ip_address: str
# list_name: str  #The list this IP address was found on
# added_date: datetime.date #The date this was added
# ASN: Optional[str] #The BGP ASN number this address is part of

async def main():

    utc_now = datetime.datetime.now(datetime.timezone.utc)

    ip_addr = Ip(
        ip_address="1.11.62.188",
        list_name="https://lists.blocklist.de/lists/all.txt",
        added_date=utc_now,
        ASN="notset"
        )

    await ip_addr.save()

    results = await ip_addr.get(ip_addr.pk)

    print(results)

if __name__ == "__main__":

    asyncio.run(main())