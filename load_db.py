import psycopg2
from helper import get_files
from loguru import logger
from config import db_config

clean_files = get_files('clean_data')

with psycopg2.connect(dbname=db_config['dbname'], 
                      user=db_config['user'], 
                      password=db_config['password']) as conn:
    cur = conn.cursor()
    cur.execute('truncate table point_log;')
    conn.commit()

    for file in list(clean_files): 
        logger.info(f'Loading {file} into DB')
        with open(file, 'r') as file:
            next(file)
            cur.copy_from(file, 'point_log', sep=',', columns=('player', 'team', 'season', 'data_date', 'points'))

        conn.commit()
