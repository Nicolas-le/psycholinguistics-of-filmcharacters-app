# The Personality of Gangsters

## Web App - Researching Quentin Tarantino’s Character Design with the Use of Computer Based Psycholinguistic Analysis.

This Repo documents the web application of a research concerning the automated analysis of film scripts.
The app is meant to be a visualization of the outcome and a tool for own questions and researches.


> **2.6 Web-App and database**
>The web application was created by using “flask”, “HTML” and “CSS”, “d3”, “jquery” and “plotly”. Concerning the displayed graph, the edges are drawn in relation to the weight. The main feature is built by the underlying relational database which is filled with all the data generated as explained above. Database tables are for example “film”, “character”, “charts”, “network results” etc. The whole database and the app are coded to sustain the extensibility of the database.

The app is a product of various NLP based analyzes that are stored in a SQlite database. **Because of copyright issues this database is not included at the moment.**/* The git concerning the analysis will be created soon.


> EN: This work was realized as part of the course "Drama Mining und Film-Analyse" (summer semester 2019) under the supervision of Manuel Burghardt and Jochen Tiepmar at the University of Leipzig.

### Use

`git clone https://github.com/Nicolas-le/Psycholinguistics-of-Filmcharacters.git`

`cd Psycholinguistics-of-Filmcharacters`

`pip3 install -r requirements.txt`

`python3 run.py`

--> go to http://127.0.0.1:5000/

### /* Until the copyright issues are solved the database structure is documented in here.

```CREATE TABLE film ( 
film_ID INTEGER NOT NULL PRIMARY KEY, 
title VARCHAR(30) NOT NULL UNIQUE, 
director VARCHAR(30), 
year INTEGER)

CREATE TABLE character (
nameC varchar(40),
text TEXT,
film_ID INTEGER,
PRIMARY KEY (nameC,film_ID),
FOREIGN KEY (film_ID) REFERENCES film)

CREATE TABLE structureGraph (
graph_ID varchar(2),
person1 varchar(40),
person2 varchar(40),
weight INTEGER NOT NULL,
film_ID INTEGER,
PRIMARY KEY (graph_ID,person1,person2),
FOREIGN KEY (film_ID) REFERENCES film)

CREATE TABLE networkResults (
algorithm varchar(30),
character varchar(40),
value FLOAT,
film_ID INTEGER,
PRIMARY KEY (algorithm,character,film_ID),
FOREIGN KEY (film_ID) REFERENCES film)

CREATE TABLE chart (
chart_ID varchar(4),
info varchar(30),
label varchar,
value INTEGER,
nameC varchar(40),
film_ID INTEGER,
PRIMARY KEY (chart_ID,info,label,film_ID),
FOREIGN KEY (nameC) REFERENCES character,
FOREIGN KEY (film_ID) REFERENCES film)


```


