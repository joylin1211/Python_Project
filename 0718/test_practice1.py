import numpy as np
from numpy import ndarray
import pandas as pd
from pandas import DataFrame

scores: ndarray | None = None
scores_df: DataFrame | None = None

scores = np.random.randint(50, 101, size=(50, 5))
scores_df = pd.DataFrame(scores,
            columns=['國文', '英文', '數學', '地理', '歷史'],
            index=range(1, 51))

names_df: DataFrame = pd.read_csv('students.csv')
scores_df[['姓名', '性別']] = names_df[['姓名', '性別']].head(n=50).values
scores_df = scores_df[['姓名', '性別', '國文', '英文', '數學', '地理', '歷史']]
print(scores_df)
