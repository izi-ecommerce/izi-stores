#!/usr/bin/env python
import os

from setuptools import find_packages, setup

setup(
    name='izi-stores',
    version="1.0-dev",
    url='https://github.com/izi-ecommerce/izi-stores',
    author="Daniel Do",
    author_email="dotiendiep@gmail.com",
    description="An extension for IZI-core to include stores",
    long_description=open(
        os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    keywords="django, izi, e-commerce",
    license='BSD',
    platforms=['linux'],
    packages=find_packages(exclude=["sandbox*", "tests*"]),
    include_package_data=True,
    install_requires=[
        'django-izi>=2.0',
        'requests>=1.1',
    ],

    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ])
