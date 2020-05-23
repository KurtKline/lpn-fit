# lpn-fit
Data cleaning and conversion for LPN Fitness Challenge

**Cleaning**  
`cleaning.py` takes csv files as input and outputs csvs that are in a suitable format to load into PostgreSQL. 

**Loading**  
`loading.py` loads cleaned csvs into PostgreSQL. 

**Next steps**
1) Set-up FastAPI locally and test functionality
2) Create PostgreSQL db on AWS
3) Load data into PostgreSQL db (from local PC)
4) Update connection strings on API to prepare for push to AWS
5) Deploy on AWS (Maybe Lambda, Elastic Beanstalk, not sure)
6) Test functionality
7) Figure out how to make it available to others
