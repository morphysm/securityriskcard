import json
from pathlib import Path

from securityriskcard import convert_to_risk

if __name__ == "__main__":
    p = Path(".")
    for fp in p.iterdir():
        if fp.name.endswith(".json") and "_risk" not in fp.name:
            with open(fp, "r") as f:
                data = json.load(f)
            result = convert_to_risk(data)
            with open(fp.with_name(fp.stem + "_risk.json"), "w") as f:
                json.dump(result, f, indent=4)
