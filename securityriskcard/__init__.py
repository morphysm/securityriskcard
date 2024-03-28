import re

MIN_SCORE = 0
MAX_SCORE = 10
RE_REASON = re.compile(r"(-- score normalized to) \d+")

RISK_TO_WEIGHT = {"Critical": 10, "High": 7.5, "Medium": 5, "Low": 2.5}
CHECK_TO_RISK_WEIGHT = {
    "Binary-Artifacts": RISK_TO_WEIGHT["High"],
    "Branch-Protection": RISK_TO_WEIGHT["High"],
    "CI-Tests": RISK_TO_WEIGHT["Low"],
    "CII-Best-Practices": RISK_TO_WEIGHT["Low"],
    "Code-Review": RISK_TO_WEIGHT["High"],
    "Contributors": RISK_TO_WEIGHT["Low"],
    "Dangerous-Workflow": RISK_TO_WEIGHT["Critical"],
    "Dependency-Update-Tool": RISK_TO_WEIGHT["High"],
    "Fuzzing": RISK_TO_WEIGHT["Medium"],
    "License": RISK_TO_WEIGHT["Low"],
    "Maintained": RISK_TO_WEIGHT["High"],
    "Pinned-Dependencies": RISK_TO_WEIGHT["Medium"],
    "Packaging": RISK_TO_WEIGHT["Medium"],
    "SAST": RISK_TO_WEIGHT["Medium"],
    "Security-Policy": RISK_TO_WEIGHT["Medium"],
    "Signed-Releases": RISK_TO_WEIGHT["High"],
    "Token-Permissions": RISK_TO_WEIGHT["High"],
    "Vulnerabilities": RISK_TO_WEIGHT["High"],
    "Webhooks": RISK_TO_WEIGHT["Critical"],
}


# @TODO: Add all the proper types?
def calculate_score(checks: list) -> float:
    total, score = 0, 0
    for check in checks:
        # Ignore 'inconclusive' score (-1).
        if check["score"] < MIN_SCORE:
            continue

        weight = CHECK_TO_RISK_WEIGHT[check["name"]]
        total += weight
        score += weight * check["score"]
    # Just in case we have no checks, lets avoid division by zero.
    return round(score / total, 1) if total > 0 else 0


def _convert_check(check: dict) -> dict:
    if check["score"] != -1:
        check["score"] = round(MAX_SCORE - check["score"], 1)
        check["reason"] = RE_REASON.sub(rf"\1 {check['score']}", check["reason"])
    return check


def _filter_check(check: dict, ignore_cii_badge: bool) -> bool:
    # @NOTE: Here we are ignoring the gimmic (badge) check, so we don't need to bother displaying
    #        it nor will we want to confuse LLM at any point to count this as a meaningful risk.
    #                                                                       - andrew, March 26 2024
    if ignore_cii_badge:
        return check["name"].lower() != "cii-best-practices"
    return True


def convert_to_risk(data: dict, ignore_cii_badge=True) -> dict:
    data["checks"] = [_convert_check(check) for check in data["checks"] if _filter_check(check, ignore_cii_badge)]
    data["score"] = calculate_score(data["checks"])
    return data
