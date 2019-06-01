from setuptools import setup, find_packages

setup(
    name='HelloWorld',
    version='1.4',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Library for DPP lab 10',
    long_description=open('README.md').read(),
    install_requires=[''],
    url='https://github.com/Karolina-Madej/DPP_Library',
    author='Karolina',
    author_email='madejkaarolina@gmail.com'
)