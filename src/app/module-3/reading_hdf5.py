import pandas as pd

h5 = pd.HDFStore("./data.h5", "r")

data_copy = h5["data"]

print(data_copy.info())

h5.close()


# more flexible method to work with HDFS
data_copy_2 = pd.read_hdf("./data/data_2.h5", "data_2")

print(data_copy_2.info())
