class DBManager:

    def __init__(self,dbname):
        self.dbname = dbname
        print(self.dbname)

        """
        if there is no db with named dbname.db here.
            self.create_db()

        """
    
    def add(self,*args):
        print("Add..")
        raise NotImplementedError

    def delete(self,*args):
        raise NotImplementedError

    def update(self,*args):
        raise NotImplementedError

    def create_db(self,*args):
        raise NotImplementedError

    def __enter__(self):
        # Open db process
        print("Connected...")
        return self

    def __exit__(self,exc_type,exc_value,tb):
        # Exit db connection
        if tb is None:
            # No exception
            # commit db
            print("Exitted...")
        else:
            # Exception occurred
            print(exc_type)
            print(exc_value)
            print(tb)
                    
        
# fill inside this class bashir.
class CalculatorDBManager(DBManager):
    pass
        

db_conn = DBManager("file_name.db")
with db_conn as db:
    db.add()
    #... operations
    pass