from unittest import TestCase
from quote_gen.app import Quote, RandomQuoteGenerator
from quote_gen.db import DB

class TestQuote(TestCase):
    def test_init(self):
        q = {
            'quote': 'Hello',
            'author': 'Ram'
        }
        qo = Quote(**q)
        self.assertEqual(qo.quote,q['quote'])
        self.assertEqual(qo.author,q['author'])

    def test_str(self):
        q = {
            'quote': 'Hello',
            'author': 'Ram'
        }
        qo = Quote(**q)
        actual = str(qo)
        expected = 'Hello\n\t\t-  Ram\n'
        self.assertEqual(actual,expected,msg=f'{actual}!= {expected}')

    def test_record(self):
        q = {
            'quote': 'Hello',
            'author': 'Ram'
        }
        expected = {
            'source': 'unknown',
            'source_type': None
        }
        expected.update(q)
        qo = Quote(**q)
        actual = qo.__record__()
        for key,value in expected.items():
            self.assertEqual(actual[key],value)



class TestFunction(TestCase):
    def setUp(self):
        q = {
            'quote': 'Hello',
            'author': 'Ram'
        }
        qo = Quote(**q)
        db = DB()
        db.insert_row( qo.__record__() )
        q = {
            'quote': 'Hi',
            'author': 'Hari'
        }
        qo = Quote(**q)
        db.insert_row( qo.__record__() )
        q = {
            'quote': 'Hello',
            'author': 'Ram'
        }
        qo = Quote(**q)
        q = {
            'quote': 'Dai',
            'author': 'Deva'
        }
        qo = Quote(**q)
        db.insert_row(qo.__record__())
        q = {
            'quote': 'Velakenna',
            'author': 'Appa'
        }
        qo = Quote(**q)
        db.insert_row(qo.__record__())
        self.db = db
        self.db.commit()

    def test_generate_rand(self):
        get_rand = RandomQuoteGenerator()
        elems = [ next(get_rand) for i in range(4) ]
        elems = [i['quote'] for i in elems]
        elems = set(elems)
        self.assertEqual(len(elems),4)


    def tearDown(self):
        import os
        os.remove("quotes.txt")



