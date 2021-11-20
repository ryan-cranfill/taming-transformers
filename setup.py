from distutils.core import setup
from setuptools import find_packages

setup(
    name='taming',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
    # packages=['taming', 'scripts', 'configs'],
    url='',
    license='',
    author='CompVis',
    author_email='',
    description=''
)
