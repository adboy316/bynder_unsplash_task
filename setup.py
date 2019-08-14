from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='unsplash',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Ariel Delgado',
    author_email='adboy316@yahoo.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

