const MIN_SCORE: number = 0;
const MAX_SCORE: number = 10;
const RE_REASON: RegExp = /(-- score normalized to) \d+/;

enum RiskLevel {
  Critical = 10,
  High = 7.5,
  Medium = 5,
  Low = 2.5,
};

const CHECK_TO_RISK_WEIGHT: Record<string, RiskLevel> = {
  "Binary-Artifacts": RiskLevel.High,
  "Branch-Protection": RiskLevel.High,
  "CI-Tests": RiskLevel.Low,
  "CII-Best-Practices": RiskLevel.Low,
  "Code-Review": RiskLevel.High,
  "Contributors": RiskLevel.Low,
  "Dangerous-Workflow": RiskLevel.Critical,
  "Dependency-Update-Tool": RiskLevel.High,
  "Fuzzing": RiskLevel.Medium,
  "License": RiskLevel.Low,
  "Maintained": RiskLevel.High,
  "Pinned-Dependencies": RiskLevel.Medium,
  "Packaging": RiskLevel.Medium,
  "SAST": RiskLevel.Medium,
  "Security-Policy": RiskLevel.Medium,
  "Signed-Releases": RiskLevel.High,
  "Token-Permissions": RiskLevel.High,
  "Vulnerabilities": RiskLevel.High,
  "Webhooks": RiskLevel.Critical,
};

interface Check {
  name: string;
  score: number;
  reason: string;
  details: string[];
}

// @TODO: Incomplete type, there is metadata and other stuff.
interface Data {
  checks: Check[];
  score: number;
}


export function calculateScore(checks: Check[]): number {
  let total: number = 0;
  let score: number = 0;
  checks.forEach((check) => {
    if (check.score < MIN_SCORE) return;
    const weight: number = CHECK_TO_RISK_WEIGHT[check.name];
    total += weight;
    score += weight * check.score;
  });
  return total > 0 ? Math.round((score / total) * 10) / 10 : 0;
}

function convertCheck(check: Check): Check {
  if (check.score !== null && check.score !== -1) {
    check.score = Math.round(MAX_SCORE - check.score);
    check.reason = check.reason.replace(RE_REASON, `$1 ${check.score}`);
  }
  return check;
}

function filterCheck(check: Check, ignoreCiiBadge: boolean): boolean {
  if (ignoreCiiBadge) {
    return check.name.toLowerCase() !== "cii-best-practices";
  }
  return true;
}

export function convertToRisk(data: Data, ignoreCiiBadge: boolean = true): Data {
  data.checks = data.checks.filter((check) => filterCheck(check, ignoreCiiBadge)).map(convertCheck);
  data.score = calculateScore(data.checks);
  return data;
}
