
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

    def run_query(self, query_statment):
        try:
            self.cur.execute(query_statment)
        except psy.Error as e:
            print(e.pgerror)
            self.conn.rollback()
            self.conn.close()
        except:
            print("Following query failed: \n", query_statment)
            self.conn.rollback()
            self.conn.close()

    def create_order_table(self):
        """
        If the table containing customer order information doesn't
        exsits this creates it.
        """
        create_orders_query = ("CREATE TABLE IF NOT EXISTS orders ("
                                "order_id bigint,"
                                "order_json json"
                                ");")
        self.run_query(create_orders_query)

    def insert_order_json(self, json):
        """
        Assumes json comes in format of key "orders" followed by
        an array of order information.
        """

        insert_order_query = ("WITH all_orders (order_info) AS (SELECT * FROM json_array_elements(%s::json->'orders')) "
                              "INSERT INTO orders (order_id, order_json) "
                              "(SELECT CAST(order_info->>'id' AS bigint), * FROM all_orders);")
        query = self.cur.mogrify(insert_order_query, (json,)) # so that we can avoid SQL injection attacks if need be
        self.run_query(query)

    def drop_order_table(self):
        drop_orders_query = ("DROP TABLE orders;")
        self.run_query(drop_orders_query)

    def create_user_table(self):
        """
        If the table containing customer order information doesn't
        exsits this creates it.
        """
        create_orders_query = ("CREATE TABLE IF NOT EXISTS users ("
                                "user_id bigint,"
                                "products_bought integer,"
                                "purchases_made integer,"
                                "amount_spent decimal,"
                                "products_per_purchase decimal,"
                                "expenditure_per_purchase decimal,"
                                "PRIMARY KEY(user_id));")
        self.run_query(create_orders_query)

    def extract_user_data(self):
        """
        Takes the order information and extracts summary metrics 
        that would be usful to business analysts
        """

        #per-user information
        user_order_query = ("INSERT INTO users (user_id, products_bought, purchases_made, amount_spent, products_per_purchase, expenditure_per_purchase) "
                            "SELECT user_id, products, purchases, spent_amt, "
                            "products/purchases::float, spent_amt/purchases::float "
                            "FROM (SELECT user_id, SUM(items.qty) AS products, "
                            "count(*) AS purchases, "
                            "SUM(CAST(order_json->>'total_price' AS decimal)) AS spent_amt "
                            "FROM orders, ("
                            "SELECT CAST(order_json->>'user_id' as bigint) as user_id, "
                            "CAST(json_array_elements(order_json->'line_items')->>'quantity' as smallint) as qty "
                            "FROM orders) as items "
                            "GROUP BY user_id) AS per_user")
        self.run_query(user_order_query)


















