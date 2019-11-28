import pandas as pd
from faker import Faker
import itertools
import random


fake = Faker("en")

profile = fake.profile()

job = fake.job()
company = fake.company()
ssn = fake.ssn()
residence = fake.address()
current_location_lat = fake.latitude()
current_location_long = fake.longitude()
blood_group = "".join(random.choice(list(itertools.product(["A", "B", "AB", "O"], ["+", "-"]))))


profile = {"job": job, "company": company, "ssn": ssn, "residence": residence, "location": ([current_location_lat, current_location_long]), "blood group": blood_group}

print(profile)
df = pd.DataFrame.from_dict(profile)

print(df.head())

