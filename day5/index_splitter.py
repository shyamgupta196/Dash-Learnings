# %%
import pandas as pd
import datetime as dt

df = pd.read_csv('TSLA.csv', parse_dates=True)

# %%
#
# pd.to_datetime(df['Date'],inplace=True)
# df['Date'] = df['Date'].astype('O')
df.dtypes

# %%

# df.set_index(['Date'], inplace=True)
# %%

df.head()
# %%


# # indexes = df.index.str.split('-')
# # print(len(indexes))
# # repl_index = []
# # for i in range(len(indexes)):
# #     app= indexes[i][0]
# #     repl_index.append(app)
# # df['years']  = repl_index   
# df.set_index(['years'],drop=True,inplace=True)    

df.set_index('years',inplace=True)
print(df.head())
# df.to_csv('TSLA.csv')
