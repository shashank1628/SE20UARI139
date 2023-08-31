import asyncio
import websockets

async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Client: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Server: {response}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main()) 
