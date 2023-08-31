import asyncio
import websockets

async def receive_message():
    uri = "ws://localhost:8888"
    async with websockets.connect(uri) as websocket:
        message = await websocket.recv()
        print("Received message from server:", message)

asyncio.get_event_loop().run_until_complete(receive_message())
