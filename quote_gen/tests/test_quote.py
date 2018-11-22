from unittest import TestCase
from quote_gen.app import Quote

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


