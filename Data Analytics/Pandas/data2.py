import pandas as pd

def run():
    data = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0], name='Numbers')
    print(data)

run()