from app.data_generator import generate_sample_dat
import sqlite3 as sql3
import datetime

start_gen = datetime.datetime.now()
data = generate_sample_dat(5e6, 5, "1min").round(4)
end_gen = datetime.datetime.now()
duration_gen = end_gen - start_gen
print(f'data gen duration: {duration_gen}')


con = sql3.connect('./data/data.sql')



start = datetime.datetime.now()
data.to_sql('data', con)
end = datetime.datetime.now()
duration = end - start
print(f'data gen duration: {duration}')