
import psycopg2 as psy
import os

class PSQL_Manager:

    def __init__(self, dbname="brow_beauty_brow",
                       user="benjamin_ramsay",
                       password=os.environ['GLOSSIER_HW_PSWD'],
                       host=os.environ['GLOSSIER_HW_SERVER'],
                       port=5432
                       ):

        try:
            conn = psy.connect(
                dbname = dbname,
                user = user,
                password = password,
                host = host,
                port = port
                )
        except:
            print("Unable to connect to database")
        cur = conn.cursor()

    def populate_orders(self, json_order):
        self.create_order_table()
        self.insert_json(json_order)

    def create_order_table(self):
        create_orders_query = ('CREATE TABLE IF NOT EXISTS orders ('
                                'order_id integer,'
                                'order_json json'
                                ');')
        cur.execute(create_orders_query)

    def insert_json(self, json):
        """
        Assumes json comes in format of key "orders" followed by
        an array of order information
        """

        insert_query = ()



















