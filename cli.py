from quote_gen.app import RandomQuoteGenerator, Quote
from quote_gen.config import get_config

from pathlib import Path

import argparse

VERSION = "0.2"


def parse_cli_args():
    parser = argparse.ArgumentParser(description="Display a random quote from a list of available quotes")
    parser.add_argument("--add-quote", action="store_true")
    parser.add_argument("--create-database", action="store_true")
    return parser.parse_args()


def get_multiline():
    print("""Your text can spawn multiple lines.\nPress ctrl+D when done.""")
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
    main()
