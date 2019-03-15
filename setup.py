import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shlink",
    version="0.0.4",
    author="David Southgate",
    author_email="d@davidsouthgate.co.uk",
    description="Python package for API communication with Shlink",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/davidksouthgate/shlink-py/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
