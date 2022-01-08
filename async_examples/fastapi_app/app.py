# Client code from: https://github.com/raphaelauv/fastAPI-aiohttp-example/blob/master/src/fastAPI_aiohttp/fastAPI.py

import asyncio
from socket import AF_INET
from typing import Optional, Any

import aiohttp
from fastapi import FastAPI
from fastapi.logger import logger

fastAPI_logger = logger
SIZE_POOL_AIOHTTP = 100


class SingletonAiohttp:
    sem: Optional[asyncio.Semaphore] = None
    aiohttp_client: Optional[aiohttp.ClientSession] = None

    @classmethod
    def get_aiohttp_client(cls) -> aiohttp.ClientSession:
        if cls.aiohttp_client is None:
            timeout = aiohttp.ClientTimeout(total=2)
            connector = aiohttp.TCPConnector(family=AF_INET, limit_per_host=SIZE_POOL_AIOHTTP)
            cls.aiohttp_client = aiohttp.ClientSession(timeout=timeout, connector=connector)

        return cls.aiohttp_client

    @classmethod
    async def close_aiohttp_client(cls) -> None:
        if cls.aiohttp_client:
            await cls.aiohttp_client.close()
            cls.aiohttp_client = None

    @classmethod
    async def query_url(cls, url: str) -> Any:
        client = cls.get_aiohttp_client()

        try:
            async with client.post(url) as response:
                if response.status != 200:
                    return {"ERROR OCCURED" + str(await response.text())}

                json_result = await response.json()
        except Exception as e:
            return {"ERROR": e}

        return json_result


async def on_start_up() -> None:
    fastAPI_logger.info("on_start_up")
    SingletonAiohttp.get_aiohttp_client()


async def on_shutdown() -> None:
    fastAPI_logger.info("on_shutdown")
    await SingletonAiohttp.close_aiohttp_client()


app = FastAPI(docs_url="/", on_startup=[on_start_up], on_shutdown=[on_shutdown])

import aiohttp

api_url = f'http://slow_api:8051/'


@app.api_route('/')
async def index(delay: int = 1):
    response = await SingletonAiohttp.query_url(f'{api_url}?delay={delay}')
    print(response)
