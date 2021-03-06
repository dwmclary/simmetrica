from setuptools import setup

setup(
    name='simmetrica',
    py_modules=['simmetrica'],
    version='0.5.0',
    description='Library for collecting, aggregating and visualizing event '
                'metrics as timeseries data',
    author='Osman Ungur',
    author_email='osmanungur@gmail.com',
    url='https://github.com/import/simmetrica',
    install_requires=['redis','flask','pyyaml'],
    tests_require=['mock'],
)
