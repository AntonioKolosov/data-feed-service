"""
Test router. You may use it for tests with API
"""


from fastapi import APIRouter
import httpx
# import asyncio


router = APIRouter()


# Redirect to the integrator
@router.get("/webdata/{lang}")
async def getweb_data(lang):
    print('getweb_data')
    api_url = f'http://127.0.0.1:8005/webdata/{lang}'
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.json()


# Redirect to the integrator
@router.get("/push/{message}")
async def push_to_connected_websockets(message: str):
    api_url = f'http://127.0.0.1:8005/push/{int(message)}'
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.json()

# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await notifier.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await websocket.send_text(f"Message text was: {data}")
#     except WebSocketDisconnect:
#         notifier.remove(websocket)

# @router.get("/push/{message}")
# async def push_to_connected_websockets(message: str):
#     await notifier.push(message)


# class Notifier:
#     def __init__(self):
#         self.connections: List[WebSocket] = []
#         self.generator = self.get_notification_generator()
#         self.first = True

#     async def get_notification_generator(self):
#         while True:
#             message = yield
#             await self._notify(message)

#     async def push(self, msg: str):
#         if self.first:
#             await self.generator.asend(None)
#             self.first = False
#         await self.generator.asend(msg)

#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         self.connections.append(websocket)

#     def remove(self, websocket: WebSocket):
#         self.connections.remove(websocket)

#     async def _notify(self, message: str):
#         living_connections = []
#         while len(self.connections) > 0:
#             # Looping like this is necessary
#             # in case a disconnection is handled
#             # during await websocket.send_text(message)
#             websocket = self.connections.pop()
#             await websocket.send_text(message)
#             living_connections.append(websocket)
#         self.connections = living_connections


# notifier = Notifier()
