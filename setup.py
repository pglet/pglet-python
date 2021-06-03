import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pglet",
    py_modules=['pglet'],
    version="0.1.0",
    license="MIT",
    author="Appveyor Systems Inc.",
    author_email="hello@pglet.io",
    description="Pglet client for Python - easily build interactive web apps in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pglet/pglet-python",
    packages=setuptools.find_packages(exclude=("tests",)),
    python_requires='>=3.7',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
)