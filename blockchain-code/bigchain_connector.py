from bigchaindb_driver import BigchainDB

from bigchaindb_driver.crypto import generate_keypair

import json


class BlockChain:
    def __init__(self):
        tokens = {}
        tokens['app_id'] = '764af86d'
        tokens['app_key'] = 'e416ddf812ab8b6196bc772280e7bea5'
        self.bdb = BigchainDB('https://test.ipdb.io', headers=tokens)

        self.alice = generate_keypair()
        self.bob = generate_keypair()

    def write_mock(self):
        with open('tx.json', 'r') as file:
            return json.load(file)

    def write(self, data):
        bdb = self.bdb
        alice = self.alice

        metadata = {'region': 'EU-central'}

        prepared_creation_tx = bdb.transactions.prepare(
            operation='CREATE',
            signers=alice.public_key,
            asset=data,
            metadata=metadata,
        )

        fulfilled_creation_tx = bdb.transactions.fulfill(
            prepared_creation_tx, private_keys=alice.private_key
        )

        sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)

        return fulfilled_creation_tx

    def get_tx(self, key):
        return self.bdb.transactions.retrieve(txid=key)
