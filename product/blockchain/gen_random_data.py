from faker import Faker
from faker.providers import misc, internet, address, company


class Gen:
    def __init__(self):
        self.faker = Faker('de_DE')
        self.faker.add_provider([misc, internet, address, company])

    def generate_random_data(self):
        faker = self.faker
        data = {
            'data': {
                'asset': {
                    'producer': {
                        "name": faker.company(),
                        'location': faker.address()
                    },
                    'materials': [
                        faker.uuid4(),
                        faker.uuid4()
                    ],
                    'batch_id': faker.uuid4(),
                    'product_id': faker.uuid4()
                },
            },
        }
        return data
