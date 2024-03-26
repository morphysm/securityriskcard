import re

MAX_SCORE = 10
RE_REASON = re.compile(r"(-- score normalized to) \d+")


def _convert_check(check: dict):
    if check["score"] not in (None, -1):
        check["score"] = round(MAX_SCORE - check["score"], 1)
        check["reason"] = RE_REASON.sub(rf"\1 {check['score']}", check["reason"])
    return check


def _filter_check(check: dict):
    # @TODO: Here we are ignoring the gimmic (badge) check, so we don't need to bother displaying
    #        it nor will we want to confuse LLM at any point to count this as a meaningful risk.
    #        However, with this change the total risk might not properly add up to 10, which is
    #        very unlikely to happen anyways so we are not as affected right now, but fixing it
    #        long term is probably a good idea.                               - andrew, March 26 2024
    return check["name"].lower() != "cii-best-practices"


def convert_to_risk(data: dict):
    if data["score"] is not None:
        data["score"] = round(MAX_SCORE - data["score"], 1)

    data["checks"] = [_convert_check(check) for check in data["checks"] if _filter_check(check)]
    return data
