from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_loadcontrols/__init__.py
from custom_loadcontrols import __version__ as version

setup(
	name="custom_loadcontrols",
	version=version,
	description="customisation",
	author="shiva",
	author_email="dev13shiva@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
