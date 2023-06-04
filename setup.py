"""
setup.py is a module used to build and distribute Python packages. 
It typically contains information about the package, such as its name, version, and dependencies, 
as well as instructions for building and installing the package.
"""

import setuptools

# reading README file so that it will help to write the description automatically if we publish this project as a module /package
with open("README.md","r",encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text-Summarization"
AUTHOR_USER_NAME = "Avinav09"
SRC_REPO = "Text_Summarizer"
AUTHOR_EMAIL = "avinav.sharma500@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization end to end project implementation.",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)