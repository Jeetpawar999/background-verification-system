import json

FILE = "app/state/execution_store.json"


def save_state(data):

    with open(FILE, "w") as f:
        json.dump(data, f)


def load_state():

    try:

        with open(FILE) as f:
            return json.load(f)

    except:

        return {}