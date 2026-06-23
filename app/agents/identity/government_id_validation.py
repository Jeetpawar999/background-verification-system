import asyncio


def validate_government_id(government_id: str):

    if not government_id:

        return {
            "status": "FAIL",
            "message": "Government ID is missing"
        }

    if len(government_id) < 8:

        return {
            "status": "FAIL",
            "message": "Government ID must be at least 8 characters"
        }

    return {
        "status": "PASS",
        "message": "Government ID validated successfully"
    }


async def run(data):

    await asyncio.sleep(1)

    government_id = data.get(
        "government_id",
        ""
    )

    result = validate_government_id(
        government_id
    )

    return {

        "agent":
            "Government ID Validation",

        "status":
            result["status"],

        "message":
            result["message"]
    }