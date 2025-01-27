from setuptools import find_packages, setup


setup(
    name='babylon',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'torch'
    ]
)