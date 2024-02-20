import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import os
import sys
project_path = '../_PAN_Project'
data_path = os.path.join(project_path, 'src', 'functions')
sys.path.append(data_path)

from PAN_functions_dt import create_artist_popularity_df

import xgboost as xgb 
from sklearn.metrics import root_mean_squared_error
color_pal = sns.color_palette()
plt.style.use('fivethirtyeight')


# The PAN_index_final dataset
pan_df = pd.read_csv('../PAN_index_final.csv', parse_dates=['Date'])


################# XGBoost ######################

pan_df = pan_df.set_index('Date').copy()

train = pan_df.loc[pan_df.index < '2023-06-01']
test = pan_df.loc[pan_df.index >= '2023-06-01']

FEATURES = ['Hot100 Rank', 'Digital Rank', 'Radio Rank', 'Streaming Rank',
       'Hot100 Peak Position', 'Digital Peak Position', 'Radio Peak Position',
       'Streaming Peak Position', 'Hot100 Weeks in Charts',
       'Digital Weeks in Charts', 'Radio Weeks in Charts',
       'Streaming Weeks in Charts']
TARGET = ['Popularity Index Scaled']

X_train = train[FEATURES]
y_train = train[TARGET]

X_test = test[FEATURES]
y_test = test[TARGET]

model = xgb.XGBRegressor(
    n_estimators=1000, 
    early_stopping_rounds=50, 
    learning_rate=0.01
    )

model.fit(X_train, y_train,
          eval_set=[(X_train, y_train), (X_test, y_test)],
          verbose=True)

# feature importances
fi_pan = pd.DataFrame(
        data = model.feature_importances_,
        index = model.feature_names_in_,
        columns=['Feature Importance']
        )


model.predict(X_test)
test['Prediction'] = model.predict(X_test)

# Concatenate the DataFrames
pan_df_concatenated = pd.concat([train, test], axis=0)

#root mean squared error
score = root_mean_squared_error(test['Popularity Index Scaled'],test['Prediction'])