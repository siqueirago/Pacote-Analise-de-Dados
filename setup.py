# setup.py

from setuptools import setup, find_packages

setup(
    name='my_data_analysis_package',
    version='0.0.1',
    description='A simple data analysis package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Julio Siqueira',
    author_email='siqueiragomes123@gmail.com',
    url='https://github.com/siqueirago/my_data_analysis_package',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
