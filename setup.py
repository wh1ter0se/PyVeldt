from setuptools import find_packages, setup

setup(
    name='pyveldt',
    packages=find_packages(include=['PyVeldt']),
    version='0.0.0',
    description='A library implementation of the Veldt LED system',
    author='wh1ter0se',
    license='AGPL-3.0',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)