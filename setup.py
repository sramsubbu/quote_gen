from setuptools import setup

def get_version(file_path):
    with open(file_path) as fp:
        for line in fp:
            line = line.strip()
            if line.startswith('__version__'):
                version_string = line.split('=')[1]
                version = eval(version_string)
                return version

setup(
    name='quote_gen',
    version= get_version('quote_gen/__init__.py'),
    packages=['quote_gen',
              'quote_gen.tests'],
    py_modules=['cli'],
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
