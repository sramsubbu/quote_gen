from setuptools import setup
from quote_gen import config 



def get_version(file_path):
    with open(file_path) as fp:
        for line in fp:
            line = line.strip()
            if line.startswith('__version__'):
                version_string = line.split('=')[1]
                version = eval(version_string)
                return version

def create_app_folder():
    app_folder = config._DEFAULT_QGEN_PATH
    print(f"checking if the app folder exists in {app_folder}")
    if app_folder.exists():
        return
    print(f'Creating app folder ...')
    app_folder.mkdir()

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

create_app_folder()
