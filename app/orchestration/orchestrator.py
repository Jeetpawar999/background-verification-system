import asyncio

from app.agents.identity.name_validation import run as name_check
from app.agents.identity.dob_verification import run as dob_check
from app.agents.identity.address_verification import run as address_check


async def execute_verification(data):

    results = await asyncio.gather(
        name_check(data),
        dob_check(data),
        address_check(data)
    )

    return {
        "status": "completed",
        "results": results
    }