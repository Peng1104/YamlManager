from setuptools import setup, find_packages

setup(
    name="YamlManager",
    version="1.0.0",
    author="Peng1014",
    author_email="admin@peng1104.net",
    description="A simple package for managing JSON and YAML files.",
    long_description=open('README.md').read(),
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