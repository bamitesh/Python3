import numpy as np
import pandas as pd
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())

data = np.array([[1, 2], [3, 4]])
print(data)

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(df)