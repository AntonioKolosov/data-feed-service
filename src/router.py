"""
Test router. You may use it for tests with API
"""


from mimetypes import guess_type
from typing import Optional
from fastapi import APIRouter

# Websocket
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from src.loader import load_content
from src.notifier import notifier


router = APIRouter()



@router.get("/app/{page}")
@router.get("/app/{page}/{script}")
async def get_script(page: str, script: Optional[str] = 'index.html'):
    print(f'get_script - {page} - {script}')
    filename = f'static/{page}/{script}'
    content = '' 
    with open(filename) as f:
        content = f.read()
    content_type, _ = guess_type(filename)
    return HTMLResponse(content, media_type=content_type)


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
