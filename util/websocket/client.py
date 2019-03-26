import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send(message)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
