execution_store = {}


def save_state(run_id, state):

    execution_store[run_id] = state


def get_state(run_id):

    return execution_store.get(run_id)


def get_all_states():

    return execution_store