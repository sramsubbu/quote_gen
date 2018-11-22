from .db import DB

from random import randint


class Quote:
    __fields__ = ['quote','author','source','source_type']

    def __init__(self,quote, author, source="unknown",
                 source_type=None):
        self.quote = quote
        self.author = author
        self.source = source
        self.source_type = source_type

    def __record__(self):
        return {field:getattr(self,field) for field in self.__fields__}

    def __repr__(self):
        return f'<Quote object>'

    def __str__(self):
        quote_string = f'{self.quote}\n\t\t-  {self.author}\n'
        source = '' if self.source =='unknown' else f'[{self.source}]'
        return f'{quote_string}{source}'


def get_random_quote():
    db_obj = DB()
    records = db_obj.fetch_all()
    start,stop = 0, len(records)
    row_id = records[ randint(start,stop) ]
    record = db_obj.fetch_single(row_id)
    db_obj.close()
    return record





