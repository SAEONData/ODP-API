from setuptools import setup, find_namespace_packages

version = '1.0.0'

setup(
    name='ODP-API',
    version=version,
    description='The Open Data Platform API',
    url='https://github.com/SAEONData/ODP-API',
    author='Mark Jacobson',
    author_email='mark@saeon.ac.za',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    python_requires='~=3.8',
    install_requires=[
        'fastapi',
        'requests',
        'python-dotenv',
    ],
    extras_require={
        'test': ['pytest', 'coverage']
    },
    dependency_links=[
        'git+https://github.com/SAEONData/ODP-AccountsLib.git#egg=ODP_AccountsLib',
    ],
)
