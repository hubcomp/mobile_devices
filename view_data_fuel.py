#%%
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv('data/dataset.csv')

#%%
df.loc[df['asset'] == 76]

#%%
MDI_OBD_FUEL = df['MDI_OBD_FUEL']
data_MDI_OBD_FUEL = []

for data in MDI_OBD_FUEL:
    if math.isnan(data):
        continue
    else:
        data_MDI_OBD_FUEL.append(data)
max_value = max(data_MDI_OBD_FUEL)
min_value = min(data_MDI_OBD_FUEL)
print(max_value,min_value)
print(len(data_MDI_OBD_FUEL))



#%%
x = np.array(data_MDI_OBD_FUEL)
x = x/x.mean()
x_std = np.std(x)
x_mean = x.mean()
print(x_mean)
print(x_std)


#%%
b = np.arange(0.0, 5, 0.001)
plt.hist(x,b)
plt.show()