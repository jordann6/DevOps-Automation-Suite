from setuptools import setup, find_packages

setup(
    name="devops_cli",
    version="1.0.0",
    packages=find_packages(include=["cli_tool", "cli_tool.*"]),  
    install_requires=[],
    entry_points={
        "console_scripts": [
            "devops-cli=cli_tool.devops_cli:main"  
        ]
    },
    author="Jordan Nelson",
    description="A simple CLI tool to scaffold DevOps projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
