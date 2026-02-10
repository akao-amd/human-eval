from pathlib import Path
from setuptools import setup, find_packages

reqs = []
for line in Path(__file__).with_name("requirements.txt").read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#"):
        reqs.append(line)

setup(
    name="human-eval",
    py_modules=["human-eval"],
    version="1.0",
    packages=find_packages(),
    install_requires=reqs,
)

