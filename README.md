# Project Summary

Sparkify, a startup with a new streaming app, wants to analyze users' behavior in terms of their music preferences. For that,
a **PostegreSQL** database was developed to analyze collected data on songs and user activity. The currently data is being saved as json files. The database consists of four dimension tables and one fact table. Three dimension tables where created from the songs and log data gathered by Sparkify, the fourth dimension table, the time table was created by extracting the timestamp field from the log data and thus deriving specific time units for later analysis. The fact table, which containerizes important information about the other dimension tables, facilitates the further analysis of the now centralized data.

The extraction, transformation and load of the json files (the raw data) was done with **Python**. The data, as already mentioned, was saved in **PostreSQL**, an open-source relational database management system (RDBMS). For this purpose serveral python libraries and modules were used.   

## How to run the Python scripts
In order to be able to run the provided python scripts, the following criteria needs to be fulfilled:
- Python version 3.6.3 or higher needs to be installed.
- It is highly recommeded to install the necessary Python libraries in an virtual environment.
- Acces to a stable version of PostgreSQL and be able to connect to it without any issues.

There are three main python scripts which were used to create and populate the PostgreSQL database required by Sparkify. There are:
1. the *sql_queries.py* script: this script gathers some of the most important data manipulation language and data definition language commands needed to not only create our database, but also to populate it with data from the log and song files.
2. the *create_tables.py* script: in this script we make full use of the Python **psycopg2** library. This library enables us to connect to our PostgreSQL database, run queries saved in our *sql_queries.py* script and commit all our changes to the database. This script is very important when trying to catch up errors and test our improvement. This script need to be run every time changes to the scripts were done.
3. the *etl.py* script: once the tables have been created, we proceed to extract, transform and load (ETL) the data into our database. This script functions as the orchestration engine between the raw data and the PostgreSQL database. It relies heavily on the logic we develop on the *sql_queries_py* script. Once this script has been run, the PostgreSQL database is created and populated with clean data.


