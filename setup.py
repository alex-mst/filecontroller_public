import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="filecontroller",
    version="1.0.1",
    description="FileController - The best user-friendly file manager",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Alex M.",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    py_modules=["filecontroller"],
    package_dir={'': 'src'},
)