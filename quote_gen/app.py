from .db import DB
from .config import get_config

from random import shuffle
import pickle


class QuotesNotAvailable(Exception):
    pass


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

    def save_to_db(self):
        db_obj = DB()
        db_obj.insert_row(self.__record__())
        db_obj.commit()


class RandomQuoteGenerator:
    PATH = get_config('PICKLE_PATH')

    def __init__(self):
        self.obj_path= RandomQuoteGenerator.PATH
        self.seq = None
        try:
            with open(self.obj_path,'rb') as fp:
                self.seq = pickle.load(fp)
        except FileNotFoundError:
            #the file does not exist. either the file is not created
            # or the file has been moved/deleted. this event needs to be logged.
            pass
        self.db = DB()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.seq:
            records = self.db.fetch_all()
            if not records:
                raise QuotesNotAvailable("No records in the DB")
            self.seq = records
            shuffle(self.seq)
        row_id = self.seq.pop()
        qparams = self.db.fetch_single(row_id)
        return Quote(**qparams)

    def close(self):
        with open(self.obj_path,'wb') as fp:
            pickle.dump(self.seq, fp)






