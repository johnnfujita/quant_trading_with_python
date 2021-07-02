import random
from math import exp, sqrt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
import quandl as q

S0 = 100
r = 0.05
T = 1.0
sigma = 0.2

values = []

for _ in range(1000000):
    ST = S0 * exp((r - 0.5 * sigma ** 2) * T +
                    sigma * random.gauss(0, 1) * sqrt(T))
    values.append(ST)


S0 = 100
r = 0.05
T = 1.0
sigma = 0.2

ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.random.standard_normal(1000000) * np.sqrt(T))


plt.style.use('seaborn')
mlp.rcParams['font.family'] = 'serif'


q.ApiConfig.api_key = QUANDL_API_KEY
d = q.get('BCHAIN/MKPRU')
d['SMA'] = d['Value'].rolling(100).mean()
d.loc['2013-1-1':].plot(title='BTC/USD exchange rate',
                        figsize=(10, 6))

plt.show()