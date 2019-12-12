def sql_query_gen():
    def __init__(self,type,default_table):
        pass

    def select(self,table):
        self.select = "SELECT * FROM" + table + ";"
        pass

    def amt(self,query=self.select):
        return len(curs.execute(query).fetchall())

    def report(self):
        pass

    querty

    def commit(self):
        self.curs.close()
        self.conn.commit()
