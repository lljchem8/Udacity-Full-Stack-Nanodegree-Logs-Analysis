# Udacity-fsnd-log-analysis

Udacity Full Stack NanoDegree Log Analysis Project

## Description

create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## How to run

1. Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip this file after downloading it. The file inside is called newsdata.sql

2. Set up the database:

   - To load the data using the command: `psql -d news -f newsdata.sql`
   - Use `psql -d news` to connect to database

3. run the python program to print out the report:
   `python query.py`
