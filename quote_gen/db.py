import json
from copy import deepcopy
from pathlib import Path
DB_PATH = "quotes.txt"


class DB:
    def __init__(self):
        self.db_path = Path(DB_PATH)

        if not self.db_path.exists():
            self.data = {}

        else:
            with open(self.db_path) as fp:
                self.data = json.load(fp)

    @classmethod
    def _hash_object(cls, obj):
        str_rep = str(obj)
        obj_hash = hash(str_rep)
        return str(obj_hash)

    def insert_row(self, row):
        row_id = self._hash_object(row)
        self.data[row_id] = row
        return row_id

    def delete_row(self, row_id):
        self.data.pop(row_id)

    def update_row(self, row_id, row):
        self.data[row_id] = row

    def fetch_single(self, row_id):
        row = self.data[row_id]
        #we need the row to be deepcopied because any changes to the row,
        # need to be updated via update_row() API only. giving access to the
        # actual db object might be violating that principle.
        return deepcopy(row)

    def fetch_all(self):
        return list( self.data.keys() )

    def query(self, query_dict):
        #the query dict can only contain exact matches. they cannot contain ranges
        # or any other selector objects, since this function does not support
        # conditional operators other than equality
        def cmp(x,y):
            for key,value in x.items():
                if value != y[key]:
                    return False
            return True
        for item in self.data:
            if cmp(query_dict,item):
                return deepcopy(item)

        return {}



    def commit(self):
        with open(self.db_path, 'w') as fp:
            json.dump(self.data, fp, indent=4)

