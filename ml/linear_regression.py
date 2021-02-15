import os
import joblib
import pandas as pd


class LinearRegression:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.model = joblib.load(dir_path + "/linear_regression.joblib")

    def preprocessing(self, input_data):
        print(input_data)
        # Turn the input data into Pandas DataFrame?

    def predict(self, input_data):
        return self.model.predict(input_data)
