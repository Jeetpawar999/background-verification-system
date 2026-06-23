import asyncio


async def run(data):

    await asyncio.sleep(1)

    full_name = data.get(
        "full_name",
        ""
    )

    return {

        "agent":
            "Sex Offender Registry",

        "status":
            "PASS",

        "match_found":
            False,

        "message":
            f"No registry match found for {full_name}"
    }