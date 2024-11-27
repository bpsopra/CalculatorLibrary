import calculator
import pandas as pd
import numpy as np
import random


# Load data

df = pd.read_excel('default_of_credit_card_clients_V2.xls',header = 0)
df = df.rename(columns={"DEFAULT": "Y"})

# Data processing
df[['PAY_0','PAY_2']] = df[['PAY_0','PAY_2']].apply(lambda x: x/1000)

# Data normalization
string_cols = ["ID","SEX","EDUCATION","MARRIAGE","Y"]


for col in string_cols:
    df[col] = df[col].astype(str)

print("STRING COLS:",df[string_cols].dtypes)

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
print("NUMERIC COLS:",numeric_cols)
print(df[numeric_cols].dtypes)


L_rand_nums = random.sample(range(1, 100), 2)
constant = calculator.add(L_rand_nums[0],L_rand_nums[1])

df_numeric = df[numeric_cols]
df_numeric["PAY_0"] = df_numeric["PAY_0"] .apply(lambda x: x + constant)
df_numeric_normalized = (df_numeric-df_numeric.min())/(df_numeric.max()-df_numeric.min())

df_normalized_all = pd.concat([df[string_cols],df_numeric_normalized], axis= 1)

# Get 5 first rows
print(df_normalized_all.head())

