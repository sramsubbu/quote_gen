from quote_gen.app import RandomQuoteGenerator, Quote
from quote_gen.config import get_config

from pathlib import Path

import argparse
import sys

VERSION = "0.2"


class App:
    # new app object
    def __init__(self, qgen_path = None):
        if qgen_path is not None:
            pass # not yet implemented
        self.get_config = get_config
        self.version = VERSION
        self.prog_name = "quote_gen"

    def add_quote(self):
        qargs = {}
        qargs['quote'] = get_multiline("Enter the quote:")
        qargs['author'] = input("Author:")
        qargs['source'] = input("Source(''): ")

        qargs = {key: value.strip() for key, value in qargs.items() if value.strip()}

        qobj = Quote(**qargs)
        db_path = self.get_config('DB_PATH')
        qobj.save_to_db(db_path)

    def print_random_quote(self):
        pickle_file_path = self.get_config('PICKLE_PATH')
        rand_gen = RandomQuoteGenerator(pickle_file_path)
        # REVIEW COMMENT: use context manager
        quote = next(rand_gen)
        print(quote)
        rand_gen.close()

    
        



# REVIEW COMMENT: Add logging to the code for debugging if needed 
# REVIEW COMMENT: Make the config to be read once and use that in various places
# REVIEW COMMENT: Handle signals, stdout, stderr, exit codes in the code if not provide justification for not handling


def parse_cli_args():
    # REVIEW COMMENT: add an option to export the quotes to a file
    # REVIEW COMMENT: add an option to display the current version of the app
    # REVIEW COMMENT: add unix style single options
    parser = argparse.ArgumentParser(description="Display a random quote from a list of available quotes")
    parser.add_argument("-a", "--add-quote", action="store_true")
    parser.add_argument("-c", "--create-database", action="store_true")
    return parser.parse_args()


def get_multiline(input_msg=''):
    msg_template = f'{input_msg}\nYour text can spawn multiple lines.\nPress ctrl+D when done.'
    print(msg_template)
    user_input = []
    while True:
        try:
            temp = input("")
        except EOFError:
            break
        else:
            user_input.append(temp)
    return '\n'.join(user_input)


def main_new():
    def create_database():
        db_path = get_config('DB_PATH')
        with open(db_path, 'w') as fp:
            print('{}', file=fp)
        print(db_path)
        
    args = parse_cli_args()
    app = App()
    if args.create_database:
        # create the db file and quit
        create_database()
        return
    if args.add_quote:
        app.add_quote()
        return
    app.print_random_quote()
        
    


def main():
    args = parse_cli_args()
    if args.create_database:
        db_path = Path(get_config('DB_PATH'))
        with open(db_path, 'w') as fp:
            print('{}', file=fp)
        print(db_path)
    if args.add_quote:
        qargs = {}
        print("Enter the quote:")
        qargs['quote'] = get_multiline()
        qargs['author'] = input("Author:")
        qargs['source'] = input("Source(''): ")

        qargs = {key: value.strip() for key, value in qargs.items() if value.strip()}

        qobj = Quote(**qargs)
        qobj.save_to_db()
    else:
        get_rand = RandomQuoteGenerator()
        quote = next(get_rand)
        print(quote)
        get_rand.close()


if __name__ == '__main__':
    main_new()
