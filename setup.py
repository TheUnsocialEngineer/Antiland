from setuptools import setup, find_packages

setup(
    name="Antiland",
    version="0.85",
    packages=find_packages(),
    install_requires=[
        "json",
        "base64",
        "threading",
        "num2words",
        "datetime",
        "aiohttp",
        ],
)
