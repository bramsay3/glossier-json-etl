
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
        self.cur = conn.cursor()

    def populate_orders(self, json_order):
        self.create_order_table()
        self.insert_order_json(json_order)

    def create_order_table(self):
        create_orders_query = ("CREATE TABLE IF NOT EXISTS orders ("
                                "order_id integer,"
                                "order_json json"
                                ");")
        self.cur.execute(create_orders_query)

    def insert_order_json(self, json):
        """
        Assumes json comes in format of key "orders" followed by
        an array of order information.
        """

        insert_order_query = ("WITH all_orders (order_data) AS (SELECT * FROM json_array_elements(%s::json->'orders'))"
                        "INSERT into orders (order_id, order_json VALUES"
                        "(SELECT * FROM all_orders),"
                        "(SELECT order_data->'id' FROM all_orders))")

        self.cur.execute(insert_order_query, (json,)


















