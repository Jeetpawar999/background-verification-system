def generate_report(results):

    overall = "PASS"

    for item in results.values():

        if item["status"] == "FAIL":
            overall = "FAIL"

    return {
        "overall_status": overall,
        "details": results
    }