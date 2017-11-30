#%%
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv('data/dataset.csv')

#%%
MDI_OBD_ENGINE_COOLANT_PRESSURE = df['MDI_OBD_ENGINE_COOLANT_PRESSURE']
data_COOLANT_PRESSURE =[]

for data in MDI_OBD_ENGINE_COOLANT_PRESSURE:
    if math.isnan(data):
        continue
    else:
        data_COOLANT_PRESSURE.append(data)
max_value = max(data_COOLANT_PRESSURE)
min_value = min(data_COOLANT_PRESSURE)
print(max_value,min_value)

#%%
print(len(data_COOLANT_PRESSURE))

total = 0
for data in MDI_OBD_ENGINE_COOLANT_PRESSURE:
    if data<2000:
        total+=1
print(total)
plt.hist(data_COOLANT_PRESSURE,[0,100,2000])
plt.show()

#%%
x = np.array(data_COOLANT_PRESSURE)
x = x/x.mean()
x_std = np.std(x)
x_mean = x.mean()
print(x_mean)
print(x_std)

#%%
b = np.arange(0.0, 0.0004, 0.00001)
n, bins, patches = plt.hist(x,b)
print(sum(n))
plt.show()

#%%
b = np.arange(0.0004, 0.0006, 0.000001)
n, bins, patches = plt.hist(x,b)
print(sum(n))
plt.show()

#%%
b = np.arange(0.0006, 0.005, 0.00001)
n, bins, patches = plt.hist(x,b)
print(sum(n))
plt.show()

