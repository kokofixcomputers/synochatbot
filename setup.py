from setuptools import setup, find_packages

setup(
    name='synochat',
    version='1.0',
    author='kokofixcomputers',
    packages=find_packages(),
    install_requires=[
        'flask==3.0.3',
        'requests==2.31.0'
    ],
)
