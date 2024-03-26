import json
from pathlib import Path

from securityriskcard import convert_to_risk


def load_test_data(variant: str):
    data_path = Path("./test_data")

    with open(data_path / f"{variant}.json", "r") as f:
        raw_data = json.load(f)

    with open(data_path / f"{variant}_risk.json", "r") as f:
        expected_result = json.load(f)

    return raw_data, expected_result


def test_regression_convert_to_risk_klocc():
    input_data, result_data = load_test_data("klocc")

    result = convert_to_risk(input_data)
    assert result == result_data


def test_regression_convert_to_risk_telethon():
    input_data, result_data = load_test_data("telethon")

    result = convert_to_risk(input_data)
    assert result == result_data


def test_regression_convert_to_risk_ansible():
    input_data, result_data = load_test_data("ansible")

    result = convert_to_risk(input_data)
    assert result == result_data


def test_regression_convert_to_risk_autogpt():
    input_data, result_data = load_test_data("autogpt")

    result = convert_to_risk(input_data)
    assert result == result_data
