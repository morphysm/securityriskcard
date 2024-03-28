# SecurityRiskCard

This package provides an simple shared way of converting security scorecard data from "wellness" into risk.
Available in:
- [Python (PyPi)](#python)
- [Typescript (NPM)](#typescript)

## Python
### Installing

To install from PyPi:
```bash
pip install securityriskcard
```

If you want to install directly from source, you can do that by adding the following into your `requirements.txt`:
```
git+https://github.com/morphysm/securityriskcard.git@main
```

### Usage example:
```python
from securityriskcard import convert_to_risk

# Your scorecard result goes here.
data = convert_to_risk(scorecard_data)
print(json.dumps(data, indent=4))
```
Or if you want to test if the package is installed and you have scorecard result as json file:
```bash
python -m securityriskcard <path/to/scorecard.json>
```

## Typescript
### Installing

To install from NPM:
```bash
npm i --save securityriskcard
```

### Usage example
```typescript
import { convertToRisk } from 'securityriskcard'

// Your scorecard result goes here.
const data = convertToRisk(scorecardData)
console.log(data);
```

## Testing

Currently packages contain some regression tests, which you can run during development or refactor to ensure data is output the same.
The directory with test data also includes a script to generate output to 'freeze' current state. Do not run it until you are confident that change behaves as expected.
