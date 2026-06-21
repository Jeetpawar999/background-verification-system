import asyncio

async def run(data):

    await asyncio.sleep(2)

    return {
        "agent": "Address Verification",
        "status": "PASS"
    }