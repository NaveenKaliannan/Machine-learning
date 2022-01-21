
import numpy as np
import pandas as pd

## prints the maximum output
pd.set_option('display.max_rows', None)

## file read
df_faa = pd.read_csv("faa_ai_prelim.csv")

## sort to find the right ones
print(np.sort(list(df_faa.columns)))

df_new = df_faa[['ACFT_MAKE_NAME','LOC_STATE_NAME','ACFT_MODEL_NAME','RMK_TEXT','FLT_PHASE','EVENT_TYPE_DESC','FATAL_FLAG']]
print(df_new.head())
df_new['FATAL_FLAG'].fillna(value='No', inplace=True)
print(df_new.head())


print(df_new.shape)
df_final = df_new.dropna(subset=['ACFT_MAKE_NAME'])
print(df_final.shape)

freq=df_final.groupby('ACFT_MAKE_NAME')
print(freq.size())

freq=df_final.groupby('FATAL_FLAG')
print(freq.size())

print(freq.get_group('Yes'))


for position,name in enumerate(df_faa.columns.values):
    df_faa[name].fillna(value='No',inplace=True)
    #print(position, name, df_faa.head())



    









