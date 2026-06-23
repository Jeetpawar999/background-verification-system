import asyncio


def validate_address(address: str):

    if not address:

        return {
            "status": "FAIL",
            "message": "Address is missing"
        }

    address = address.strip()

    if len(address) < 5:

        return {
            "status": "FAIL",
            "message": "Address is too short"
        }

    return {
        "status": "PASS",
        "message": "Address verified successfully"
    }


async def run(data):

    await asyncio.sleep(1)

    address = data.get(
        "address",
        ""
    )

    validation_result = validate_address(
        address
    )

    return {

        "agent":
            "Address Verification",

        "status":
            validation_result["status"],

        "message":
            validation_result["message"],

        "address":
            address
    }