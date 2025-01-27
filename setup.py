from setuptools import find_packages, setup


setup(
    name='babylon',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    include_package_data=True,
    package_data={
        "babylon": ["render.js"]
    }
)