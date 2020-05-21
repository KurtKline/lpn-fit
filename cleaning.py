import pandas as pd 
import numpy as np
from datetime import date


def convert_date(data_date: str, year: int = 2014): 
    month, day = data_date.split('/')
    return date(year, int(month), int(day))

df = pd.read_csv('lpn_fit.csv')
columns = ['player', 'date', 'points']
new_df = pd.DataFrame(columns=columns)

date_cols = df.columns[1:]
for index, row in df.iterrows():
    for date_col in date_cols:
        if not pd.isnull(row[date_col]):
            clean_date = convert_date(date_col)
            new_df = new_df.append({'player': row['players'], 
                                    'date': clean_date, 
                                    'points': row[date_col]}, ignore_index=True) 

print(new_df)


