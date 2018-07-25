"""
Setup module for PyPI.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# With a little witchcraft, we can use README.rst as long description for PyPI
def get_readme():
    with open('README.rst', encoding='UTF-8') as readme:
        return readme.read()

setup(
    name='buildvu',
    version='2.1.0',
    description="Python API for IDRSolutions' Buildvu Microservice Example",
    long_description=get_readme(),
    url='https://github.com/idrsolutions/buildvu-python-client',
    author='IDRSolutions',
    author_email='support@idrsolutions.zendesk.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        # Development Status:: 5 - Production / Stable
        # Development Status:: 6 - Mature
        # Development Status:: 7 - Inactive
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='idrsolutions pdf html5 converter buildvu microservice example web '
             'application server API python client',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
    # package_data={
    #     'sample': ['package_data.dat'],
    # },
    # data_files=[('my_data', ['data/data_file'])],
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
    project_urls={
        'Source': 'https://github.com/idrsolutions/buildvu-python-client/',
        'Tracker': 'https://github.com/idrsolutions/buildvu-python-client/issues',
        'Contact us': 'https://idrsolutions.zendesk.com/hc/en-us/requests/new'
    },
)
