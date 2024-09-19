"""Setup script for the YamlManager package."""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="YamlManager",
    version="1.2.2",
    author="Peng1014",
    author_email="admin@peng1104.net",
    description="A simple package for managing JSON and YAML files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Peng1104/YamlManager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
