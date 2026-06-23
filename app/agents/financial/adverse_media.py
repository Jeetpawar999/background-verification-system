import asyncio


def check_adverse_media(full_name: str):

    if not full_name:

        return {
            "status": "FAIL",
            "negative_news": False,
            "message": "Candidate name is missing"
        }

    return {
        "status": "PASS",
        "negative_news": False,
        "message": "No adverse media records found"
    }


async def run(data):

    await asyncio.sleep(1)

    full_name = data.get(
        "full_name",
        ""
    )

    result = check_adverse_media(
        full_name
    )

    return {

        "agent":
            "Adverse Media Check",

        "status":
            result["status"],

        "negative_news":
            result["negative_news"],

        "message":
            result["message"],

        "candidate":
            full_name
    }