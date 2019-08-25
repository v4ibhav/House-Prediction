import pandas as pd

newt = pd.read_csv('Y_prednew.csv')
# newt.head()

newt["Id"] = newt["Id"] + 1101

# newt.head()
# newt.to_csv('Y_prednew.csv')

