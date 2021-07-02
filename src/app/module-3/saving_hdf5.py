import pandas as pd
from app.data_generator import generate_sample_dat

data = generate_sample_dat(rows=5e6, cols=10).round(4)

# more flexible way to deal with hdfs
data.to_hdf('./data/data_2.h5', 'data_2', format='table')


print(data.info())

h5 = pd.HDFStore('./data.h5', "w")
h5['data'] = data

print(h5)
h5.close()