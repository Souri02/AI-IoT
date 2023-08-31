import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        print("Received message:", message)
        response = "Message received successfully!"
        await websocket.send(response)

start_server = websockets.serve(handle_connection, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
