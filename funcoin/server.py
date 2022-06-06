import asyncio
from asyncio import IncompleteReadError, exceptions
from codecs import StreamReader, StreamWriter

class Server:
    
    def __init__(self, blockchain, connection_pool, p2p_procol):
        ...
    
    async def get_external_ip(self):
        # Finds out "external IP" so that we can advertize it to our peers
        ...

    async def get_external_ip(self):
        while True:
            try:
                # Handle and/or reply to the incoming data
                ...
            except(asyncio.exceptions.IncompleteReadError, ConnectionError):
                break

    async def listen(self, hostname="0.0.0.0", port = 8888):
        server = await asyncio.start_server(self.handle_connection, hostname, port)
        
        logger.info(f"Server listening on {hostname}:{port}")
        
        self.external_ip = await self.get_external_ip()
        self.external_port = 8888
        
        async with server:
            await server.serve_forever()