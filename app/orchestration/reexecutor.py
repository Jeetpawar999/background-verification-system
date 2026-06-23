from app.state.dependency_map import DEPENDENCY_MAP

async def reexecute(feedback):

    if "address" in feedback.lower():

        return {

            "reexecuted_agents": [
                "address_verification"
            ],

            "cached_agents": [
                "criminal",
                "financial"
            ]
        }

    return {

        "message":
            "No impacted agents found"
    }