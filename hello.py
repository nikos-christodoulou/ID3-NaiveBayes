import numpy as np
import pandas as pd
from collections import deque
from InformationGain import Entropy
data = {
    'wind_direction': ['N', 'S', 'E', 'W'],
    'tide': ['Low', 'High'],
    'swell_forecasting': ['small', 'medium', 'large'],
    'good_waves': ['Yes', 'No']
}
data_df = pd.DataFrame(columns=data.keys())

np.random.seed(42)
# randomnly create 1000 instances
for i in range(1000):
    data_df.loc[i, 'wind_direction'] = str(np.random.choice(data['wind_direction'], 1)[0])
    data_df.loc[i, 'tide'] = str(np.random.choice(data['tide'], 1)[0])
    data_df.loc[i, 'swell_forecasting'] = str(np.random.choice(data['swell_forecasting'], 1)[0])
    data_df.loc[i, 'good_waves'] = str(np.random.choice(data['good_waves'], 1)[0])

data_df.head()
print(data_df)
print(data_df.shape[1])
X = np.array(data_df.drop('good_waves', axis=1).copy())
print(X)
y = np.array(data_df['good_waves'].copy())
print(y)
feature_names = list(data_df.keys())[:3]
print(feature_names)


x_targets_count = (1,2,3,4,5,6)
id_of_category = ([1,2,3,4],[5,6,7,8])
x = [v_counts/len(id_of_category) * 0.5 for v_counts,v_ids in zip(x_targets_count,id_of_category)]
print(x)