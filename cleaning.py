import pandas as pd 
import numpy as np
from datetime import date
from pathlib import Path
from typing import List, Dict


def convert_date(data_date: str, year: int = 2014) -> date: 
    month, day = data_date.split('/')
    return date(year, int(month), int(day))

def get_files(folder: str, regex: str = '*.csv') -> Dict:
    return {filename:filename.name for filename in Path(folder).glob(regex)}

raw_files = get_files('raw_data')
columns = ['player', 'date', 'points']

for file in list(raw_files): 
    df = pd.read_csv(file)
    clean_df = pd.DataFrame(columns=columns)

    date_cols = df.columns[1:]
    for index, row in df.iterrows():
        for date_col in date_cols:
            if not pd.isnull(row[date_col]):
                clean_date = convert_date(date_col)
                clean_df = clean_df.append({'player': row['players'], 
                                            'date': clean_date, 
                                            'points': row[date_col]}, 
                                            ignore_index=True) 

    clean_df.to_csv(f'clean_data/clean_{raw_files[file]}', index=False)

