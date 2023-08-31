import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8888"
    async with websockets.connect(uri) as websocket:
        message_to_send = "Hello from the server!"
        await websocket.send(message_to_send)
        print("Server sent message:", message_to_send)

asyncio.get_event_loop().run_until_complete(send_message())
