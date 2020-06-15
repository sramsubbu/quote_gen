from quote_gen.app import RandomQuoteGenerator, Quote, export_all_quotes
from quote_gen.config import get_config
from quote_gen.db import DB
import quote_gen
import json

from pathlib import Path

import argparse
import sys

# REVIEW COMMENT: Add logging to the code for debugging if needed 
# REVIEW COMMENT: Handle signals, stdout, stderr, exit codes in the code if not provide justification for not handling
VERSION  = quote_gen.__version__


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
        db_obj = DB(db_path)
        qobj.save_to_db(db_obj)

    def export(self, output_file):
        db_path = self.get_config("DB_PATH")
        db_obj = DB(db_path)
        quotes = export_all_quotes(db_obj)
        json.dump(quotes, output_file, indent=4)

    def import_from_file(self, input_file):
        quotes = json.load(input_file)
        db_path = self.get_config('DB_PATH')
        db_obj = DB(db_path)
        for quote in quotes:
            db_obj.insert_row(quote)
        db_obj.commit()
        db_obj.close()
        print("Imported from the given file")
        

    def print_random_quote(self):
        pickle_file_path = self.get_config('PICKLE_PATH')
        db_path = self.get_config('DB_PATH')
        rand_gen = RandomQuoteGenerator(pickle_file_path, db_path)
        # REVIEW COMMENT: use context manager
        quote = next(rand_gen)
        print(quote)
        rand_gen.close()





def parse_cli_args():
    # REVIEW COMMENT: add an option to export the quotes to a file
    parser = argparse.ArgumentParser(description="Display a random quote from a list of available quotes", prog='quote_gen')
    parser.add_argument("-a", "--add-quote", action="store_true")
    parser.add_argument("-c", "--create-database", action="store_true")
    parser.add_argument("-v", "--version", action='version',version=f'%(prog)s {VERSION}')
    data_exporting = parser.add_mutually_exclusive_group()
    data_exporting.add_argument("-e", "--export", type=argparse.FileType('w'))
    data_exporting.add_argument("-i", "--import-file", type=argparse.FileType('r'))
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


def main():
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
    if args.export:
        app.export(args.export)
        return
    if args.import_file:
        app.import_from_file(args.import_file)
        return
        
    if args.add_quote:
        app.add_quote()
        return
    app.print_random_quote()
        

if __name__ == '__main__':
    main()
