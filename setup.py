# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in shippmentservice/__init__.py
from shippmentservice import __version__ as version

setup(
	name='shippmentservice',
	version=version,
	description='Use for PGL Vehicle Shippment Service',
	author='me',
	author_email='marianoor09@outlook.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
