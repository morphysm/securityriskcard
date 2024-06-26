import os

from setuptools import find_packages, setup


def read_requirements(req_path: str = "requirements.txt"):
    if not os.path.exists(req_path):
        return []

    with open(req_path, "r") as req:
        return [line.strip() for line in req if line.strip()]


setup(
    name="securityriskcard",
    version="0.0.8",
    author="Cyberfame Team",
    author_email="0x4480@cyberfame.io",
    description="Conversion from scorecard ratings to risk ratings.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/morphysm/securityriskcard",
    license="AGPL-3.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    tests_require=read_requirements("requirements-test.txt"),
)
