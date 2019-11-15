import random
import pandas as pd


path_adj = 'names_generator/list_adjective.csv'
path_sur = 'names_generator/list_surname.csv'

df_adj = pd.read_csv(path_adj, sep=',', header=0)
df_sur = pd.read_csv(path_sur, sep=',', header=0, usecols=[2])

left = df_adj['adjective'].tolist()
right = df_sur['surname'].tolist()


class GetRandomName():
    def __init__(self):
        self.left = random.choice(left)
        self.right = random.choice(right)
        self.randint = random.randint(1, 10)
        # self.retry = retry

    def random_name(self, retry):
        name = str(self.left + '_' + self.right)
        if retry > 1:
            name = str(self.left + '_' + self.right + self.randint)
        return name
