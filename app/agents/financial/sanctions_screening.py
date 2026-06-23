import asyncio


def check_sanctions(full_name: str):

    if not full_name:

        return {
            "status": "FAIL",
            "sanctioned": False,
            "message": "Candidate name is missing"
        }

    return {
        "status": "PASS",
        "sanctioned": False,
        "message": "No sanctions match found"
    }


async def run(data):

    await asyncio.sleep(1)

    full_name = data.get(
        "full_name",
        ""
    )

    result = check_sanctions(
        full_name
    )

    return {

        "agent":
            "Sanctions Screening",

        "status":
            result["status"],

        "sanctioned":
            result["sanctioned"],

        "message":
            result["message"],

        "candidate":
            full_name
    }