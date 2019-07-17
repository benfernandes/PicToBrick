from os import path

from setuptools import find_packages, setup

cwd = path.abspath(path.dirname(__file__))


def _read_file(*file_path):
    return open(path.join(cwd, *file_path), encoding="utf8").read()


setup(
    name='PicToBrick',
    version='0.0.1',
    author='Tom Johnson & Ben Fernandes',
    description='API to convert images to Lego diagrams',
    packages=find_packages(),
    long_description=_read_file('README.md'),
    entry_points={
        'console_scripts': ['ptb=pic_to_brick.cli:cli']
    },
    install_requires=[
        'attrs',
        'flask',
        'Pillow'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'pytest>=4.6',
            'pytest-mock>=1.10',
            'pytest-runner',
            'flake8',
            'mypy',
            'isort',
            'tox',
            'pyinstaller==3.4',
            'bump2version',
        ]
    },
)
