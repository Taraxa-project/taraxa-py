from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "taraxa-py"

DESCRIPTION = "Taraxa blockchain  RPC client."

KEYWORDS = "Taraxa blockchain RPC client"

AUTHOR = "Aeneas"

AUTHOR_EMAIL = "kai.he@taraxa.io"

URL = "http://taraxa.io"

VERSION = "0.0.6"

LICENSE = "MIT"

setup(
    name=NAME,
    version=VERSION,
    python_requires='>=3.7',
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=LICENSE,
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=True,
)
