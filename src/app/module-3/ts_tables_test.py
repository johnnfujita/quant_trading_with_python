from app.data_generator import generate_sample_dat

import datetime
import tstables
import tables as tb

start = datetime.datetime(2021,1,24)
end = datetime.datetime(2021, 1, 25)

class Desc(tb.IsDescription):
    timestamp = tb.Int64Col(pos=0)
    No0 = tb.Float64Col(pos=1)
    No1 = tb.Float64Col(pos=2)
    No2 = tb.Float64Col(pos=3)
    No3 = tb.Float64Col(pos=4)
    No4 = tb.Float64Col(pos=5)

data = generate_sample_dat(rows=2.5e6, cols=5, freq="1s").round(4)

print(data.info())

h5 = tb.open_file('./data/data.h5ts', 'w')
ts = h5.create_ts('/', 'data', Desc)
ts.append(data)
print(h5)


subset_1 = ts.read_range(start, end)

print(subset_1.info())

subset_2 = ts.read_range(datetime.datetime(2021, 1, 24, 12, 30, 0), datetime.datetime(2021, 1, 29, 17, 15, 30))
print(subset_2.info())
h5.close()