from app.state.dependency_map import DEPENDENCY_MAP


async def reexecute(feedback):

    feedback = feedback.lower()

    reexecuted_agents = []

    cached_agents = []

    updated_section = None

    for key, agents in DEPENDENCY_MAP.items():

        if key in feedback:

            reexecuted_agents.extend(
                agents
            )

            updated_section = "identity"

    if reexecuted_agents:

        cached_agents = [

            "criminal_verification",

            "financial_verification"
        ]

        return {

            "status": "completed",

            "execution_type": "fresh",

            "updated_section":
                updated_section,

            "reexecuted_agents":
                reexecuted_agents,

            "cached_agents":
                cached_agents,

            "message":
                "Selective re-execution completed successfully"
        }

    return {

        "status": "completed",

        "execution_type": "cached",

        "reexecuted_agents": [],

        "cached_agents": [

            "identity_verification",

            "criminal_verification",

            "financial_verification"
        ],

        "message":
            "No impacted agents found"
    }