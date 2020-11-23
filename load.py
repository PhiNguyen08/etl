from pymongo import MongoClient
import pandas as pd

class MongoDB:
    def __init__(self, db_name):
        self.db_name = db_name
        try:
            self.client = MongoClient()
            self.db = self.client[self.db_name]
            print('MongoDB Connection Successful. CHEERS!!!')
        except Exception as e:
            print('Connection Unsuccessful!! ERROR!!')
            print(e)

    def insert_into_db(self, data, collection):
        try:
            self.db[collection].insert(data)
            print('Data Inserted Successfully')
        except Exception as e:
            print('OOPS!! Something Happen ')
            print(e)

    def read_from_db(self, collection):
        try:
            data = pd.DataFrame(list(self.db[collection].find()))
            print('Data Fetched Successfully')
            return data
        except Exception as e:
            print('OOPS!! Some ERROR ')
            print(e)