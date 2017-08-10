from setuptools import setup, find_packages

setup(
    name='graphics-utils',
    version='1.0.0',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'': ['*']},
    url='https://github.com/wobeng/graphics-utils',
    license='',
    author='wobeng',
    author_email='wobeng@yblew.com',
    description='detect face and transform image',
    install_requires=[
        'numpy',
        'Pillow'
    ]
)
