# **Project 01: Data Modeling with Postgres**

## **Project Summary**

Sparkify, a startup with a new streaming app, wants to analyze users' behavior regarding their music preferences. For this purpose, a PostgreSQL database was developed to analyze the collected data on songs and user activities. The data is currently stored as json files. The database consists of four dimension tables and one fact table. Three dimension tables were created from the song and log data collected by Sparkify, and the fourth dimension table, the time table, was created by extracting the timestamp field from the log data to derive specific time units for later analysis. The fact table, which containerizes important information about the other dimension tables, facilitates further analysis of the now centralized data.

The extraction, transformation, and loading of the json files (the raw data) was performed using Python. The data was stored in PostgreSQL, an open-source relational database management system (RDBMS), as mentioned earlier. Several Python libraries and modules were used for this purpose.

## **How to run the Python scripts**

In order to be able to run the provided python scripts, the following criteria needs to be fulfilled:
- Python must be installed in version 3.6.3 or higher.
- It is highly recommended to install the necessary Python libraries in a virtual environment.
- Access to a stable version of PostgreSQL must be available to connect to it without problems.

There are three main Python scripts used to create and populate the PostgreSQL database required by Sparkify. These are:

1. the *sql_queries.py* script: this script gathers some of the main data manipulation language and data definition language commands needed to not only create our database, but also to populate it with data from the log and song files.
2. the *create_tables.py* script: in this script we make full use of the Python library psycopg2. This library allows us to connect to our PostgreSQL database, run the queries stored in our sql_queries.py script, and commit all our changes to the database. This script is very important when we are trying to find bugs and test our improvements. This script must be run every time changes are made to the scripts.
3. the *etl.py* script: once the tables are created, we proceed to extract, transform and load (ETL) the data into our database. This script acts as an orchestration engine between the raw data and the PostgreSQL database. It relies heavily on the logic we develop for the sql_queries.py script. Once this script is executed, the PostgreSQL database is populated with clean data.

## Files used in this project

The files used in this repository are all stored in the **data** folder. This folder contains the song dataset and the log dataset, both in json format.

**The song dataset**

The song dataset is a subset of the [MillionDataSet](http://millionsongdataset.com/). These files contain real metadata about songs and artists. As mentioned earlier, it is a subset that contains only the first three letters of the track ID of each song; hence the partitioning.

**The log Dataset**

Unlike the song files, which are real data, the log files are simulated files. They were created using an external tool ([event simulator](https://github.com/Interana/eventsim)). These files are divided by month; however, generated data for the month of November was used.

## Design of the database schema and ETL pipeline

**Design of the database schema**

This database was developed to contain four dimension tables and one fact table. The dimension tables were created by grouping related attributes about the numerical values in the fact table, under one dimension; this avoided duplicating data when it was not necessary. As a result, we have the following dimension tables:

- Songs
- Artists
- Users
- Time

The Songplays fact table was created to store partially denormalized data for analytical purposes. While the granularity of dimension tables is theoretically much higher, the fact table takes data with a finer grain.

**ETL Pipeline**

We wrote our ETL pipeline using Python. In doing so, we made extensive use of the **pyscopg2** library. This library allowed us to connect to our Postgres database, create a cursor to execute commands, and run all of our Python scripts from one place. To extract all the json files, perform the necessary transformations, and load the final data into our database, we created three Python scripts. Detailed explanations of the scripts and how they work can be found above in the section: **Execution of the Python Scripts**.

**ER Diagram**

Below is the resulting star schema for the Sparkify database in PostgreSQL.

<p align="center">
<img  width="726" height= "804" src=/images/sparkify_er.png alt="Sparkify ER Diagram">
</p>

## Querying the Data


```
select concat(first_name, last_name) as full_name, count(sg.song_id) as totalsongslistened
from songplays sp
join users us on (sp.user_id = us.user_id)
join songs sg on (sp.song_id = sg.song_id)
group by first_name, last_name
order by totalsongslistened desc
limit 10;
```

<p align="center">
<img  width="50%" height= "50%" src=/images/result_query1.png alt="Result to query 1">
</p>

