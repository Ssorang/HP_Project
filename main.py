import pandas as pd

df = pd.read_excel("/Users/s0rang/HP_Project/sj_covid.xlsx")
print(df[['확진일','성명']])