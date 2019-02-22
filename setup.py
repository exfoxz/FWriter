import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Fwriter",
    version="0.0.1",
    author="Sam Nguyen",
    author_email="chanhnp@gmail.com",
    description="Easy logging for training NN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/exfoxz/Fwriter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
