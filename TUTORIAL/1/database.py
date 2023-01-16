import json
from memory_profiler import profile

"""
" Memory Monitor
" https://www.geeksforgeeks.org/monitoring-memory-usage-of-a-running-python-program/
" https://pypi.org/project/memory-profiler/
" https://www.youtube.com/watch?v=LbwHoBY8vwg
" https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba
"""

class Database:
    
    def __init__(self, database) -> None:
        self.database = database
    
    @profile
    def select(self):
        try:
            with open(self.database, encoding="utf-8") as db:
                return True, json.loads(db.read())
        except Exception as err:
            return False, err
        
    @profile
    def insert(self, new):
        try:
            with open(self.database, "w") as db:
                json.dump(new, db, indent=4)
                return True, "insert success"
        except Exception as err:
            return False, err
    
    @profile 
    def update(self, data):
        try:
            with open(self.database, "w") as db:
                json.dump(data, db, indent=4)
                return True, "delete success"
        except Exception as err:
            return False, err
    
    @profile
    def delete(self, data):
        try:
            with open(self.database, "w") as db:
                json.dump(data, db, indent=4)
                return True, "delete success"
        except Exception as err:
            return False, err
        