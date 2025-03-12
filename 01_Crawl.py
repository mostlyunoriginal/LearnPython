import pandas as pd

url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df=pd.read_csv(url,header=None)