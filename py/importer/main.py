
import asyncio
import aiohttp

from datetime import datetime
import urllib.request
import shutil
from config import Importer

HOSTNAME = Importer.API_HOST

class importer():
    """
    Class to import list of IP address into database
    """
    
    def __init__(self, source_file_url=None, download_file=None, block_size=100, list_name=None, ip_api="http://localhost"):
        """
        Class initiator
        :param str source_file_url: The URL of the IP address lists we are downloading
        :param str block_size: Size of the chunks to fetch from the source file url
        :param str download_file: The file to download the contents of source_file_url
        :param str list_name: The name of the file - used to identify where the ip came from
        """
        print(f"source_file_url {source_file_url}")
        self.source_file_url=source_file_url
        self.block_size=block_size
        self.download_file=download_file
        self.list_name=list_name
        
    def _download_file(self):
        """
        Download the file to local system
        """
        if self.download_file is None:
            download_file  = self.source_file_url.split('/')[-1]
            self.download_file = download_file
        else:
            download_file = self.download_file

        with urllib.request.urlopen(self.source_file_url) as response, open(download_file, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    def _read_file_in_blocks(self, file_handle, block_size):
        """
        Read the file block at a time. this is helpful for large files
        """
        block = []
        for line in file_handle:
            block.append(line.decode().strip())
            if len(block) == block_size:
                yield block
                block = []

        # yield last block or any block under block size
        if block:
            yield block

    async def _post_ip(self, data) -> str:
        """
        Post IP address to API
        """
        print(f"data {data}")
        async with aiohttp.ClientSession() as session:
            async with session.post(
                HOSTNAME,
                json=data
            ) as resp:
                ip_addr = await resp.json()
                return ip_addr

    async def run_importer(self):
        """
        Run the import routine
        """
        self._download_file()
        with open(self.download_file, 'rb') as file_handle:
            for block in self._read_file_in_blocks(file_handle, self.block_size):
                tasks = [self._post_ip({
                            "ip_address": ip,
                            "list_name": self.list_name,
                        }) for ip in block]
                await asyncio.wait(tasks)
        

async def app() -> None:
    i = importer(
    source_file_url="https://lists.blocklist.de/lists/all.txt",
    download_file="/home/importer/block-list-all.txt",
    list_name="blocklist.de"
    )
    await i.run_importer()

if __name__ == "__main__":
    asyncio.run(app())
