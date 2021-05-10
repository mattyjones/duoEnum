import setuptools
import os
import re

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(
        os.path.join(
            HERE,
            "duoenum",
            "bin",
            "version.py"
        )
    ).read()
    return VERSION_RE.search(init).group(1)


def get_description():
    return open(
        os.path.join(os.path.abspath(HERE), "README.md"), encoding="utf-8"
    ).read()

setuptools.setup(
    name='duoenum',
    author='Matt Jones',
    author_email='urlugal@gmail.com',
    include_package_data=True,
    version=get_version(),
    description='duoenum testing',
    keywords='duo, package',
    long_description=get_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/mattyjones/duoenum',
    project_urls={
        'Documentation': 'https://github.com/mattyjones/duoenum',
        'Bug Reports':
        'https://github.com/mattyjones/duoenum/issues',
        'Source Code': 'https://github.com/mattyjones/duoenum',
    },
    packages=setuptools.find_packages(exclude=['test*']),
    install_requires=[
        'click',
        'duo_client',
    ],
    classifiers=[
        # see https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    zip_safe=True,
    # extras_require={
    #     'dev': ['check-manifest'],
    #     # 'test': ['coverage'],
    # },
    entry_points={"console_scripts": "duoenum=duoenum.bin.cli:main"},
)
