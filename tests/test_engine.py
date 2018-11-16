from quote_gen.engine import Engine
from pathlib import Path
import unittest


class TestEngine(unittest.TestCase):
    def setUp(self):
        DB_PATH = 'quotes.txt'
        obj = Path(DB_PATH)
        with open(obj,'w') as fp:
            fp.write('[]')
        self.path = obj
        self.db = Engine()


    def test_engine_create(self):
        obj1 = Engine()
        obj2 = Engine()
        self.assertEqual(id(obj1),id(obj2))

    def test_init(self):
        self.assertEqual(len(self.db.data),0)

    def test_insert(self):
        record = {'a':1,'b':2}
        rid  = self.db.insert_row(record)
        self.assertEqual(len(self.db.data),1)
        self.assertEqual(rid,0)

    # def test_update(self):
    #     record = {'a': 1, 'b': 2}
    #     rid = self.db.insert_row(record)
        rid = 0
        record = {'a':'vowel','b':'B'}
        self.db.update_row(record,rid)
        actual = self.db.data[rid]
        for key,value in actual.items():
            with self.subTest(msg=key):
                self.assertEqual(value,record[key])


    def test_delete(self):
        record = {'a': 'vowel', 'b': 'B'}
        row_id = self.db.insert_row(record)
        rows = len(self.db.data)
        row_id = rows-1
        self.db.delete_row(row_id)
        self.assertEqual(len(self.db.data),rows-1)

    def tearDown(self):
        self.path.unlink()

def engine_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestEngine))
    return suite

if __name__ == "__main__":
    unittest.main()