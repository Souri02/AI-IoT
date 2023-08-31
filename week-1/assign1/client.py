import asyncio
import websockets

async def send_message():
    uri = "ws://139.59.95.113:5000"
    async with websockets.connect(uri, timeout=10) as websocket:
        message_to_send = input("Enter your message: ")
        await websocket.send(message_to_send)
        print("Message sent")

        response = await websocket.recv()
        print("Received response:", response)

asyncio.get_event_loop().run_until_complete(send_message())
