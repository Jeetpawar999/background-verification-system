import hashlib
import json


def generate_hash(data):

    data_string = json.dumps(
        data,
        sort_keys=True,
        default=str
    )

    return hashlib.sha256(
        data_string.encode()
    ).hexdigest()