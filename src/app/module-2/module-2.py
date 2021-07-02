import csv
import pandas as pd
#PURE PYTHON
# with open("./apple.csv", 'r') as f:
    # for _ in range(5):
        # print(f.readline(), end="")

#CSV and list comprehension
# csv_reader = csv.reader(open("apple.csv", "r"))
# data = list(csv_reader)
# print(data[:5])

# CSV DICTREADER() and List Comprehension
# csv_reader = csv.DictReader(open("apple.csv", "r"))
# data = list(csv_reader)
# print(data[:2])



data = pd.read_csv("apple.csv", index_col=0, parse_dates=True)
print(data.info())
print(data.tail())
print(data["OPEN"].mean())
print(data["CLOSE"].mean())

# save to excel
data.to_excel("./apple.xls", "APPL")
data.to_json("./apple.json")

# read json and excel are also available
data_from_xls = pd.read_excel("./apple.xls", "APPL", index_col=0)
data_from_json = pd.read_json("./apple.json")
