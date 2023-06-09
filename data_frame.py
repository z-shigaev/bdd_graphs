import numpy as np
import pandas as pd
# s = pd.Series([1, 2, 3, 4, 5, 5])
# print(s)


class RawData:
    def __init__(self, path):
        self.path = path
        self.data = self.read_data()

    def read_data(self):
        try:
            data = pd.read_csv(self.path, sep=';')
        except FileNotFoundError as error:
            data = np.nan
            print(error)
        return data

    def get_headers(self):
        return self.data.columns

    def get_column(self, header):
        return self.data[header].tolist()


if __name__ == "__main__":
    test = RawData("data/test.csv")
    # print(test.data)
    print(test.get_headers())
    # print(len(test.get_headers()))
    print(test.get_column(test.get_headers()[1]))
