import asyncio
from ably import AblyRest

async def main():
    async with AblyRest('sok-YA.5to6ww:uqtEaCH_ajot8lHU') as ably:
        channel = ably.channels.get("channel_name")

if __name__ == "__main__":
    asyncio.run(main())