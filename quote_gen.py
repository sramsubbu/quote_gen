from pathlib import Path
from random import shuffle 
import sys
import json
import pickle 


QUOTE_GEN_PATH = Path.home() / ".quote_gen" 
QUOTES_JSON = QUOTE_GEN_PATH / "quotes.json" 
QUOTES_PERSIST = QUOTE_GEN_PATH / ".qpersist"



def create_and_get_random_list():
    content = get_quotes()
    quote_size = len(content)
    random_index_list = list(range(quote_size))
    shuffle(random_index_list)
    return random_index_list 


def get_random_list():
    """
    Read the qpersist file and unpickle and return the list 
    """
    with open(QUOTES_PERSIST, 'rb') as f:
        content = pickle.load(f)
    return content 


def save_random_list(random_list):
    with open(QUOTES_PERSIST, 'wb') as f:
        pickle.dump(random_list, f)


def get_quotes():
    with open(QUOTES_JSON) as f:
        return json.load(f)


def get_default_quotes():
    quote = {"quote": "Power resides where men believe it resides. It's a trick, a shadow on the wall", "author": "George RR Martin"}
    return [quote]


def print_quote(quote: dict[str,str]):
    quote_str = quote.get("quote", "")
    author = quote.get("author")
    if author is None:
        print(quote_str)
        return 
    template = """
{quote}
        -  {author}"""
    quote_str = template.format(quote=quote_str, author=author)
    print(quote_str)

def init():
    '''
    If the quote_gen folder does not exist or if required files don't exist create them
    '''
    if not QUOTE_GEN_PATH.exists():
        QUOTE_GEN_PATH.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {QUOTE_GEN_PATH}")
    if not QUOTES_JSON.exists():
        print("quotes.json file does not exist in quote_gen path. Creating with default")
        quotes = get_default_quotes()
        with open(QUOTES_JSON, 'w') as f:
            json.dump(quotes, f, indent=4)



def save_update_random_list(random_list):
    with open(QUOTES_PERSIST, "wb") as f:
        pickle.dump(random_list, f)


def main():
    init()
    random_list = None 
    if QUOTES_PERSIST.exists():
        random_list = get_random_list()
    if not random_list:
        random_list = create_and_get_random_list()
    if not random_list:
        print("No quotes yet!. Add some quotes to get started")
        return 
    quote_index = random_list.pop()
    quotes = get_quotes()
    quote = quotes[quote_index]
    print_quote(quote)
    save_update_random_list(random_list)
    

if __name__ == '__main__':
    main()

