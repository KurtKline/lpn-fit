# lpn-fit
Data cleaning and conversion for LPN Fitness Challenge

**Cleaning**  
`cleaning.py` takes csv files as input and outputs csvs that are in a suitable format to load into PostgreSQL. 

**Loading**  
`loading.py` loads cleaned csvs into PostgreSQL. 

**API**  
`lpn_app` folder contains files necessary to run FastAPI with defined end points. 

**Calling API**  
`call_api.py` is a base template for calling the API and loading into a dataframe. 

**Next steps**  
- [x] Set-up FastAPI locally and test functionality  
- [ ] Create PostgreSQL db on AWS  
- [ ] Load data into PostgreSQL db (from local PC)  
- [ ] Update connection strings on API to prepare for push to AWS  
- [ ] Deploy on AWS (Maybe Lambda, Elastic Beanstalk, not sure)  
- [ ] Test functionality  
- [ ] Figure out how to make it available to others  

