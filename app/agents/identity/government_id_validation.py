def validate_government_id(
        government_id: str
):

    if len(government_id) < 8:

        return {
            "status": "FAIL"
        }

    return {
        "status": "PASS"
    }