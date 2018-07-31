
from psql_json import PSQL_Manager
import json
import os


man = PSQL_Manager()
man.create_order_table()
prev_orders = os.listdir('orders')

#load in order data retroactively
for day_order in prev_orders:
    input_json = open('orders/' + day_order).read()
    clean_json = json.dumps(json.loads(input_json))
    man.insert_order_json(clean_json)
    man.conn.commit()

#compute BI metrics on previous orders
man.create_user_table()
man.extract_user_data()
man.conn.commit()


from psql_json import PSQL_Manager
man = PSQL_Manager()
man.create_user_table()
man.extract_user_data()
man.conn.commit()