import asyncio
import websockets

# Define a callback to handle incoming WebSocket connections
async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")
        response = f"Server: {message}"
        await websocket.send(response)

# Create a WebSocket server
start_server = websockets.serve(handle_client, "localhost", 8765)

# Start the server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever() 
