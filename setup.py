from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ArchivesSpace-Python-Client',
    version='0.1.0',
    description='Provides methods and classes that can be used when interacting with the ArchivesSpace API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AustinTSchaffer/ArchivesSpace-Python-Client',
    author='Austin T Schaffer',
    author_email='schaffer.austin.t@gmail.com',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Librarians',
        'Intended Audience :: Archivists',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='archivesspace archives api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'requests>=2.18,<3',
        'urllib3>=1.19,<2',

    ],

    package_data={},
    project_urls={
        'Bug Reports': 'https://github.com/AustinTSchaffer/ArchivesSpace-Python-Client/issues',
        'Feature Requests': 'https://github.com/AustinTSchaffer/ArchivesSpace-Python-Client/issues',
        'Source': 'https://github.com/AustinTSchaffer/ArchivesSpace-Python-Client'
    },
)