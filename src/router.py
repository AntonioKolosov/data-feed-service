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
    # api_url = f'http://127.0.0.1:8005/webdata/{lang}'
    # api_url = f'https://neat-krill-honest.ngrok-free.app/webdata/{lang}'
    api_url = f'https://messintegrator.onrender.com/webdata/{lang}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url)
        except Exception as e:
            print(e)
            return {"error": e.__cause__}
        return response.json()


# Redirect to the integrator
@router.get("/push/{message}")
async def push_to_connected_websockets(message: str):
    # api_url = f'http://127.0.0.1:8005/push/{int(message)}'
    # api_url = f'https://neat-krill-honest.ngrok-free.app/push/{int(message)}'
    api_url = f'https://messintegrator.onrender.com/push/{int(message)}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url)
        except Exception as e:
            print(e)
            return {"error": e.__cause__}
        return response.json()
