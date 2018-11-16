from quote_gen.engine import Engine,DB_PATH

class Record:
    __fields__ = []
    def __init__(self,**fields):
        pass

    def _initialise(self,**fields):
        '''
        decoupling parameter setting to allow multiple constructors
        :param fields:
        :return:
        '''
        field_list = []
        for field,value in fields.items():
            if field not in self.__fields__:
                raise AttributeError(f"{field} not a valid argument")
            setattr(self,field,value)
            field_list.append(field)

    def __record__(self):
        '''
        shorthand call to get the list of fields and their values as a dict
        :return:
        '''
        return {field:getattr(self,field) for field in self.__fields__}


class ActiveRecord(Record):
    def __init__(self,**fields):
        self.engine = Engine()
        self.id = self.engine.insert_row(self.__record__)

    def save(self):
        self.engine.update_row(self.id, self.__record__)
        self.engine.commit()

class Quote(ActiveRecord):
    __fields__ = ['quote', 'author', 'source', 'source_type']
    def __init__(self,quote,author,source="Unknown",source_type=None):
        self._initialise(quote=quote,author=author,source=source,source_type=source_type)
        super().__init__()










