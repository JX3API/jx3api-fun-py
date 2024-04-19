import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jx3apifun",
    version="0.0.1",
    author="JustUndertaker",
    author_email="806792561@qq.com",
    description="女生自用jx3api sdk for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JX3API/jx3api-fun-py",
    packages=["jx3apifun"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.9",
)
