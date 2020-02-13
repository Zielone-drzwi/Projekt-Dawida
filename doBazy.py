
from decimal import Decimal
from faker import Faker
from faker import factory
fake = Faker(['pl_PL'])
for _ in range(10):
    print(fake.latitude(),  fake.longitude())