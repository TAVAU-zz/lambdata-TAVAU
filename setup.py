from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="yuhan-package-name", # the name that you will install via pip
    version="1.0",
    author="Yuhan Wang",
    author_email="yuhanwang001@email.com",
    description="helper functions for dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/TAVAU/lambdata-TAVAU.git",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)