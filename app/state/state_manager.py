from datetime import datetime

execution_store = {}


def save_state(run_id, state):

    if run_id in execution_store:

        version = (
            execution_store[run_id].get(
                "version",
                0
            ) + 1
        )

    else:

        version = 1

    execution_store[run_id] = {

        "version": version,

        "timestamp":
            datetime.now().isoformat(),

        **state
    }


def get_state(run_id):

    return execution_store.get(
        run_id
    )


def get_all_states():

    return execution_store


def delete_state(run_id):

    if run_id in execution_store:

        del execution_store[run_id]

        return {
            "message": "State deleted successfully"
        }

    return {
        "message": "State not found"
    }