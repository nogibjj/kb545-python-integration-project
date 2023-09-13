import pandas as pd


def run_statistics(filePath):
    df = pd.read_csv(filePath)

    return df.describe()["sepal_length"]
