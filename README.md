# SecurityRiskCard

This package provides an simple shared way of converting security scorecard data from "wellness" into risk.

### Installing

We are not publishing the package to PyPi, so you to install directly from source.  
You can do that by adding the following into your `requirements.txt`:
```
git+https://github.com/morphysm/securityriskcard.git@main
```
**Note** however, that this requires you to authorize every time you install with a token.
So, if you need to install it without interaction (e.g. inside docker), use the following:
```
git+https://token:${GITHUB_TOKEN}@github.com/morphysm/securityriskcard.git@main
```
Where you just need to export a `GITHUB_TOKEN` variable during build.

### Testing

Currently package contains some regression tests, which you can run during development or refactor to ensure data is output the same.
The directory with test data also includes a script to generate output to 'freeze' current state. Do not run it until you are confident that change behaves as expected.