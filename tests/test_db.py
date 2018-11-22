
from quote_gen.db import DB, DB_PATH

from pathlib import Path
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        DB_PATH = "./test_quotes.txt"

    def test_init(self):
        obj = DB()
        self.assertEqual(len(obj.data), 0)

    def test_insert_row(self):
        obj = DB()
        row = {'name': 'Ram','occupation': "python programming"}
        self.assertEqual(len(obj.data),0)
        row_id = obj.insert_row(row)
        self.assertEqual(len(obj.data),1)
        d = obj.data[row_id]
        for key,value in d.items():
            self.assertEqual(row[key],value)

    def test_update_row(self):
        obj  = DB()
        row = {'name': 'Ram','occupation': "python programming"}
        row_id = obj.insert_row(row)
        new_row = {'name':'Ram','occupation': 'web development'}
        obj.update_row(row_id, new_row)
        d = obj.data[row_id]
        for key,value in d.items():
            self.assertEqual(new_row[key], value)

    def test_delete_row(self):
        obj = DB()
        row = {'name': 'Ram', 'occupation': "python programming"}
        row_id = obj.insert_row(row)
        self.assertEqual(len(obj.data),1)
        obj.delete_row(row_id)
        self.assertEqual(len(obj.data),0)

    def test_fetch_single(self):
        obj= DB()
        row = {'name': 'Ram', 'occupation': "python programming"}
        row_id = obj.insert_row(row)
        fr = obj.fetch_single(row_id)
        for key,value in fr.items():
            self.assertEqual(value, row[key])


    def test_fetch_all(self):
        obj = DB()
        row = {'name': 'Ram', 'occupation': 'python'}
        row2 = {'name': 'Ramin djawadi', 'occupation': 'composer'}
        r1 = obj.insert_row(row)
        r2 = obj.insert_row(row2)
        rows = obj.fetch_all()
        self.assertEqual(len(rows),2)
        for i in (r1,r2):
            self.assertIn(i, rows)


    def test_commit(self):
        obj = DB()
        row = {'name': 'Ram','occupation':'web development'}
        row_id =obj.insert_row(row)
        obj.commit()
        obj2 = DB()
        self.assertEqual(len(obj2.data), 1)

    def tearDown(self):
        test_file = Path("quotes.txt")
        if test_file.exists():
            test_file.unlink()


def create_module_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestDB))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = create_module_suite()
    runner.run(suite)