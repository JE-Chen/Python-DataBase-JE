import setuptools

with open("README.md", "r") as README:
    long_description = README.read()

setuptools.setup(
    name="JEDatabase",
    version="0.0.0.0.6",
    author="JE-Chen",
    author_email="zenmailman@gmail.com",
    description="JE use Sqlite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JE-Chen/Python_DataBase_JE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Traditional)",
    ]
)

# sdist bdist_wheel
# python -m twine upload dist/*
