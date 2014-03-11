from setuptools import setup

setup(name='vparse',
    version='0.1',
    description='Visually defined PDF interpretation in Python',
    url='https://github.com/sbirch/vparse',
    author='Sam Birch',
    author_email='sam.m.birch@gmail.com',
    license='MIT',
    packages=['vparse'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'])