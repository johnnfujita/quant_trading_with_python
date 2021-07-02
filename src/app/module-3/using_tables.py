import tables as tb

h5 = tb.open_file("./data/data_2.h5", "r")

print(h5)

print(h5.root.data_2.table[:3])

h5.close()