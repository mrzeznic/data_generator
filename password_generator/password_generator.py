import random
import string


def password_generator(num_of_chars):
    try:
        num_of_chars = int(num_of_chars)
        if num_of_chars >= 4:
            password_source = string.ascii_letters + string.digits + string.punctuation
            password = random.choice(string.ascii_lowercase)
            password += random.choice(string.ascii_uppercase)
            password += random.choice(string.digits)
            password += random.choice(string.punctuation)
            for i in range(num_of_chars-4):
                password += random.choice(password_source)

            password_list = list(password)
            random.SystemRandom().shuffle(password_list)
            password = ''.join(password_list)
            return password
        if num_of_chars < 4:
            raise Exception('Value must be greater than 4.')
    except ValueError:
        raise Exception(('Value not correct.'))


# print(password_generator(4))
