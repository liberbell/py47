import datetime
import pandas as pd

today = datetime.date.today()
# print(today.year, today.month, today.day)
yesterday = today - datetime.timedelta(days=1)
# print(yesterday)
# print(today.strftime("%Y/%m/%d"))
# print(datetime.datetime.now())

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df)

df = pd.read_csv("california_housing_test.csv")
print(df.iloc[: , :3])
print(df[df["housing_median_age"] > 30])
print(df.shape)
print(df.describe())