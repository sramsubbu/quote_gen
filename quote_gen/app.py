from .db import DB

from random import randint,shuffle
import pickle

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


class RandomQuoteGenerator:
    PATH = 'qpersist'

    def __init__(self):
        self.obj_path= RandomQuoteGenerator.PATH
        self.seq = None
        try:
            with open(self.obj_path,'rb') as fp:
                self.seq = pickle.load(fp)
        except FileNotFoundError:
            pass
        self.db = DB()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.seq:
            records = self.db.fetch_all()
            self.seq = records
            shuffle(self.seq)
        row_id = self.seq.pop()
        return self.db.fetch_single(row_id)

    def close(self):
        with open(self.obj_path,'wb') as fp:
            pickle.dump(self.seq, fp)






