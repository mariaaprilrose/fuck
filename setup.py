from setuptools import setup, find_packages

setup(
    name = 'tunewhale',
    version = '1.0',
    url = 'https://tunewhale.com/',
    license = 'BSD',
    description = 'Attempt at making TuneWhale.com',
    author = 'jayzces',
    author_email = 'jayzces@gmail.com',
    packages = find_packages('src/tunewhale'),
    package_dir = {'': 'src/tunewhale'},
    install_requires = ['setuptools'],
)