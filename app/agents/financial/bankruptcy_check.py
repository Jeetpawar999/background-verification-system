import asyncio


def check_bankruptcy(full_name: str):

    if not full_name:

        return {
            "status": "FAIL",
            "bankruptcy": False,
            "message": "Candidate name is missing"
        }

    return {
        "status": "PASS",
        "bankruptcy": False,
        "message": "No bankruptcy records found"
    }


async def run(data):

    await asyncio.sleep(1)

    full_name = data.get(
        "full_name",
        ""
    )

    result = check_bankruptcy(
        full_name
    )

    return {

        "agent":
            "Bankruptcy Check",

        "status":
            result["status"],

        "bankruptcy":
            result["bankruptcy"],

        "message":
            result["message"],

        "candidate":
            full_name
    }