import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = ['pymongo']
tests_require = requires + ['nose', 'coverage']

setup(
    name='strider-python-mongodb-test',
    version='1.0',
    author="Niall O'Higgins",
    author_email='niallo@beyondfog.com',
    description='Useful towel-related stuff.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=tests_require,
    test_suite="nose.collector",
)
