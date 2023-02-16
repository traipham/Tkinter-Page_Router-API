from typing import Iterable


from typing import List
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="tkinter-page-router-tpham",
    version="1.0.0",
    desciption="A tkinter page router module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Trai Pham",
    author_email="traipham16@yahoo.com",
    classifiers =[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="tkinter-router",
    py_modules=["router"],
    pytohn_requires=">=3.9.13, <4",
    install_requires=["tkinter"]
)