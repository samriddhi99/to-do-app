from setuptools import setup, find_packages

setup(
    name="mini-todo",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Flask>=2.3.0"
    ],
)
