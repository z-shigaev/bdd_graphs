import numpy as np
import pandas as pd
# s = pd.Series([1, 2, 3, 4, 5, 5])
# print(s)


class Graph:
    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(path, sep=';')


if __name__ == "__main__":
    test = Graph("data/test.csv")
    print(test.data)