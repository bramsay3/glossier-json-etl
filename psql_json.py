
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
            self.conn = psy.connect(
                dbname = dbname,
                user = user,
                password = password,
                host = host,
                port = port
                )
        except:
            print("Unable to connect to database")
        self.cur = self.conn.cursor()

    def populate_orders(self, json_order):
        self.create_order_table()
        self.insert_order_json(json_order)

    def create_order_table(self):
        create_orders_query = ("CREATE TABLE IF NOT EXISTS orders ("
                                "order_id bigint,"
                                "order_json json"
                                ");")
        self.cur.execute(create_orders_query)

    def insert_order_json(self, json):
        """
        Assumes json comes in format of key "orders" followed by
        an array of order information.
        """

        insert_order_query = ("WITH all_orders (order_info) AS (SELECT * FROM json_array_elements(%s::json->'orders')) "
                        "INSERT INTO orders (order_id, order_json) "
                        "(SELECT CAST(order_info->>'id' AS bigint), * FROM all_orders);")
        query = self.cur.mogrify(insert_order_query, (json,))
        try:
            self.cur.execute(query)
        except psy.Error as e:
            print(e.pgerror)
        except:
            print("Following query failed: \n", query)


















