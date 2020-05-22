import pandas as pd 
import numpy as np
from datetime import date
from typing import List
from helper import get_files


def convert_date(data_date: str, year: int = 2014) -> date: 
    month, day = data_date.split('/')
    return date(year, int(month), int(day))

def is_valid_entry(points) -> bool:
    if np.isnan(points) or points == 0:
        return False
    return True

def get_season(filename: str) -> str:
    return '_'.join(filename.split('_')[1:])

def get_team(filename: str) -> str: 
    return filename.split('_')[0]

raw_files = get_files('raw_data')
columns = ['player', 'team', 'season', 'date', 'points']

for file in list(raw_files): 
    df = pd.read_csv(file)
    clean_df = pd.DataFrame(columns=columns)

    date_cols = df.columns[1:]
    for index, row in df.iterrows():
        for date_col in date_cols:
            if is_valid_entry(row[date_col]):
                clean_date = convert_date(date_col, int(file.stem[-4:]))
                clean_df = clean_df.append({'player': row['player'], 
                                            'team': get_team(file.stem),
                                            'season': get_season(file.stem),
                                            'date': clean_date, 
                                            'points': row[date_col]}, 
                                            ignore_index=True) 

    clean_df.to_csv(f'clean_data/clean_{raw_files[file]}', index=False)

