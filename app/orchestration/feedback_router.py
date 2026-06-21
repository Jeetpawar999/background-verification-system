def get_affected_agents(feedback: str):

    feedback = feedback.lower()

    mapping = {
        "address": [
            "address_verification",
            "address_history_verification"
        ],
        "name": [
            "name_validation"
        ],
        "dob": [
            "dob_verification"
        ],
        "credit": [
            "credit_check"
        ]
    }

    for key, value in mapping.items():
        if key in feedback:
            return value

    return []