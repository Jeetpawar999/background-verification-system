import asyncio
import uuid

from app.agents.identity.name_validation import run as name_check
from app.agents.identity.dob_verification import run as dob_check
from app.agents.identity.address_verification import run as address_check

from app.audit.audit_logger import log_event
from app.state.state_manager import save_state


async def execute_verification(data):

    run_id = str(uuid.uuid4())

    results = await asyncio.gather(
        name_check(data),
        dob_check(data),
        address_check(data)
    )

    log_event(
        "identity_verification",
        "completed"
    )

    save_state(
        run_id,
        {
            "status": "completed",
            "results": results
        }
    )

    return {

        "run_id": run_id,

        "status": "completed",

        "cache_status": {

            "identity": "fresh",

            "criminal": "cached",

            "financial": "cached"
        },

        "results": results
    }