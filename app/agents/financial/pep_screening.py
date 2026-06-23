import asyncio

async def run(data):

    await asyncio.sleep(1)

    return {
        "agent": "PEP Screening",
        "status": "PASS"
    }