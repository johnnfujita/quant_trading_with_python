from setuptools import setup, find_packages

setup(
    name="python_trading",
    author="Johnnie Fujita",
    author_email="johnnie.fujita@gmail.com",
    license="MIT",
    version="0.1.0",
    description="python_for_trading",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},)