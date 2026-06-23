from datetime import datetime


def generate_report(results, audit_logs=None):

    overall_status = "PASS"

    risk_score = 0

    findings = []

    for item in results:

        if isinstance(item, dict):

            if item.get("status") == "FAIL":

                overall_status = "FAIL"

                risk_score += 20

                findings.append(
                    item.get(
                        "message",
                        "Verification failed"
                    )
                )

    return {

        "executive_summary":
            f"Verification completed with status {overall_status}",

        "overall_status":
            overall_status,

        "risk_score":
            risk_score,

        "key_findings":
            findings,

        "flags_and_alerts":
            findings,

        "execution_timestamp":
            datetime.now().isoformat(),

        "audit_trail":
            audit_logs if audit_logs else [],

        "cache_status": {

            "identity": "fresh",

            "criminal": "fresh",

            "financial": "fresh"
        },

        "details":
            results
    }