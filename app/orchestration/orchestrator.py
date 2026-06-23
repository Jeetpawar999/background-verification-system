import asyncio
import uuid

# Identity Agents
from app.agents.identity.name_validation import run as name_check
from app.agents.identity.dob_verification import run as dob_check
from app.agents.identity.address_verification import run as address_check

# Criminal Agents
from app.agents.criminal.federal_check import run as federal_check
from app.agents.criminal.state_check import run as state_check
from app.agents.criminal.county_check import run as county_check

# Financial Agents
from app.agents.financial.credit_check import run as credit_check
from app.agents.financial.fraud_detection import run as fraud_check
from app.agents.financial.pep_screening import run as pep_check

from app.audit.audit_logger import log_event
from app.state.state_manager import save_state


async def execute_verification(data):

    run_id = str(uuid.uuid4())

    log_event(
        "verification",
        "started"
    )

    results = await asyncio.gather(

        # Identity Verification
        name_check(data),
        dob_check(data),
        address_check(data),

        # Criminal Verification
        federal_check(data),
        state_check(data),
        county_check(data),

        # Financial Verification
        credit_check(data),
        fraud_check(data),
        pep_check(data)
    )

    log_event(
        "identity_verification",
        "completed"
    )

    log_event(
        "criminal_verification",
        "completed"
    )

    log_event(
        "financial_verification",
        "completed"
    )

    save_state(
        run_id,
        {
            "status": "completed",
            "results": results
        }
    )

    log_event(
        "report_generation",
        "completed"
    )

    return {

        "run_id": run_id,

        "status": "completed",

        "cache_status": {

            "identity": "fresh",

            "criminal": "fresh",

            "financial": "fresh"
        },

        "results": results
    }