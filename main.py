
from psql_json import PSQL_Manager
import json

input_json = open('orders/2017-10-30.json').read()
clean_json = json.dumps(json.loads(input_json))
man = PSQL_Manager()

