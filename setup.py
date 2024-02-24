from setuptools import setup, Extension

setup(
    name='lis_package',
    version='0.1',
    packages=['lis'],
    ext_modules=[Extension('lis._liblis', ['cpp_src/lis.cpp'])],
    install_requires=['numpy'],
)