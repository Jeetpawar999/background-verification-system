from datetime import datetime

audit_history = []


def log_event(agent_name, status):

    audit_history.append(
        {
            "agent": agent_name,
            "status": status,
            "timestamp": datetime.now().isoformat()
        }
    )


def get_audit_history():

    return audit_history