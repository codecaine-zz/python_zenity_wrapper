#!/usr/bin/env python3
"""Setup script for python-zenity-wrapper package."""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-zenity-wrapper",
    version="0.1.0",
    author="CodeCaine",
    author_email="",
    description="A comprehensive Python wrapper for Zenity dialogs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codecaine-zz/python_zenity_wrapper",
    packages=find_packages(),
    py_modules=["zenity_wrapper"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Environment :: X11 Applications",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses subprocess
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "zenity-wrapper-demo=demo:main",
        ],
    },
    keywords="zenity dialog gui desktop notification wrapper linux macos",
    project_urls={
        "Bug Reports": "https://github.com/codecaine-zz/python_zenity_wrapper/issues",
        "Source": "https://github.com/codecaine-zz/python_zenity_wrapper",
    },
)
