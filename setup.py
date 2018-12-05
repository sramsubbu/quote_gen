from setuptools import setup

setup(
    name='quote_gen',
    version='0.2',
    packages=[ 'quote_gen',
               'quote_gen.tests'],
    py_modules = ['cli'],
    url='',
    license='GPL',
    author='Ramasubramanian S',
    author_email='sramsubu@gmail.com',
    description='Generate a random quote from the list of available quotes',
    entry_points={
        "console_scripts": [
            "quote_gen=cli:main",
            ],
        },

)
