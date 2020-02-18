# Poc Fullstack Web Project
A good proof of concept focused on a conventional scenario in which data interacts with frontend and backend through APIS, the complet stack of the POC are below in description.

# Angular 8


# Python - flask - flask_sqlalchemy


# SQL Server
During this proof of concept I used a local server and SQL Server Express distribution, but also you can use the distribution you prefer, just change the configuration present in
api_poc_project/app/config.py

- SERVER = 'localhost\SQLEXPRESS'
- DATABASE = 'POC'
- DRIVER = 'SQL+Server'
- SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{SERVER}/{DATABASE}?driver={DRIVER}'
- SQLALCHEMY_TRACK_MODIFICATIONS = False

Also the scripts to create the tables and stored procedures are in the db_scripts folder

# How to run the entire app?
- 1) Create local DB with any distribution of SQL Server 
- 2) Execute run.py present in api_poc_project 
- 3) Use any browser to access http://127.0.0.1:5000/home

# Future improvements
- Add central log register for tracking the errors and make troubleshooting application problems easily solved.
- Add tokens to the API and management components.
- Change default port, because port 5000 its not recomended for production.
- Verify CORS politics in clients calls to the API

# Missing features
- DB stored procedures
- Views in Angular for Bill and ExternalProvider
- API's control to foreign keys

# Notes:
- All that you need from python libraries and packages it's present in requeriments.txt
- Feel in complete confidence to contribute to this project :)
