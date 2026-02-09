"""
Setup configuration for MLB Jersey RAG system.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="mlb-jersey-rag",
    version="1.0.0",
    author="MLB Jersey RAG Project",
    description="A RAG system for searching MLB team jerseys using semantic search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mlb-jersey-rag",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "chromadb==0.4.22",
        "sentence-transformers==2.3.1",
        "numpy==1.24.3",
        "pandas==2.0.3",
        "tqdm==4.66.1",
    ],
    extras_require={
        "dev": [
            "pytest==7.4.3",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    entry_points={
        "console_scripts": [
            "mlb-jersey-search=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["data/*.json"],
    },
)
