from bigchain_connector import BlockChain
from pprint import pprint
from gen_random_data import Gen

import time


db = BlockChain()

tx = db.write_mock()
pprint(tx.get('id'))

data = Gen().generate_random_data()

tx2 = db.write(data=data)
pprint(tx2)

key2 = tx2.get('id')
  
time.sleep(2)
tx3 = db.get_tx(key=key2)
pprint(tx3)
assert (tx2 == tx3)
