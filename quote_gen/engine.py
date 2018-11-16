import json
from pathlib import Path
ENGINE = None
DB_PATH = 'quotes.txt'


class Singleton(type):
    _instances = {}

    def __call__(mcs, *args, **kwargs):
        if mcs not in mcs._instances:
            mcs._instances[mcs] = super().__call__(*args,*kwargs)
        return mcs._instances[mcs]


class Engine(metaclass=Singleton):
    def __init__(self):
        self.db_path = Path(DB_PATH)

        with open(self.db_path) as fp:
            self.data = json.load(fp)

    def insert_row(self,record):
        if self.data is None:
            raise Exception("Database closed")

        id = len(self.data)
        self.data.append(record)
        return id

    def update_row(self,record,record_id):
        self.data[record_id] = record

    def delete_row(self,record_id):
        self.data.pop(record_id)

    def commit(self):
        with open(self.db_path,'w') as fp:
            json.dump(self.data,fp)
