"""
Test router. You may use it for tests with API
"""


from fastapi import APIRouter

# Websocket
from fastapi import WebSocket, WebSocketDisconnect

from src.loader import load_content
from src.notifier import notifier


router = APIRouter()


@router.get("/webdata/{lang}")
async def getweb_data(lang):
    print('getweb_data')
    doc_name = f'{lang}_data'
    content = load_content(doc_name)
    content_value = content['content']
    return {"content": content_value}


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print('websocket_endpoint')
    await notifier.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        notifier.remove(websocket)


@router.get("/push/{message}")
async def push_to_connected_websockets(message: str):
    await notifier.push(message)
