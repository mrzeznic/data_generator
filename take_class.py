from names_generator import names_generator
from password_generator import password_generator
from number_generator import phone_number_generator
from words_generator import words_generator
from hasher.hasher import hasher
from faker import Faker

# name
name_class = names_generator.GetRandomName()
print("names_generator: ")
print(name_class.random_name(1))
print("")
# tripple name
word_class = str(words_generator.gen())
print("words_generator: ")
print(word_class)
print("")
# password
password_generator = password_generator.password_generator(6)
print("password_generator: ")
print(password_generator)
print("")
# hashed password
hasher = hasher()
hash_pass = hasher.sha1(word_class)
print("password_hasher: ")
print(hash_pass)
print("")
# number
phone_class = phone_number_generator.phone_number_generator
print("phone_number_generator: ")
print(phone_class())
print("")
# street
fake = Faker("pl_PL")
print("address generator: ")
print(fake.street_address())
print("")
# city
fake = Faker("pl_PL")
print("address generator: ")
print(fake.city())
print("")

# providers profile
fake = Faker("pl_PL")
print("providers profile")
print(fake.profile())
print("")