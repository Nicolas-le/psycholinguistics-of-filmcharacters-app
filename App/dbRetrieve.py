'''
@author Nicolas Ruth, Julian Fuchs
(c) 2019

Pulls the wanted data from the database.
'''

import sqlite3
connection = sqlite3.connect("App/filmanalysis.db", check_same_thread=False)

cursor = connection.cursor()

def getEdges(title):
    sql_command = """
    SELECT G.person1, G.person2, G.weight
    FROM structureGraph AS G NATURAL JOIN film AS F
    WHERE F.title = ?
    """
    cursor.execute(sql_command,(title,))
    edges = cursor.fetchall()
    return edges

def getLabelsAndValuesChart(character,info,title):
    sql_command = """
    SELECT C.label, C.value
    FROM chart AS C NATURAL JOIN film AS F
    WHERE C.nameC = ? AND C.info = ? AND F.title = ?
    """
    cursor.execute(sql_command,(character,info,title,))
    labels = cursor.fetchall()
    return labels

def getLabelsAndValuesNetwork(algorithm,title):
    sql_command = """
    SELECT NR.character, NR.value
    FROM networkResults AS NR NATURAL JOIN film AS F
    WHERE NR.algorithm = ? AND F.title = ?
    """
    cursor.execute(sql_command,(algorithm,title,))
    labels = cursor.fetchall()
    return labels

def getText(character,title):
    sql_command = """
        SELECT C.text
        FROM character AS C NATURAL JOIN film AS F
        WHERE C.nameC = ? AND F.title = ?
        """
    cursor.execute(sql_command,(character,title,))
    text = cursor.fetchall()
    return text

def getNwResults(title,algorithm):
    sql_command = """
        SELECT C.nameC, N.value
        FROM character AS C NATURAL JOIN film AS F NATURAL JOIN networkResults AS N
        WHERE F.title = ? AND N.algorithm = ?
        """
    cursor.execute(sql_command,(title,algorithm,))
    results = cursor.fetchall()
    return results

def getAllCharacters(title):
    sql_command = """
        SELECT C.nameC
        FROM character AS C NATURAL JOIN film AS F
        WHERE F.title = ?
        """
    cursor.execute(sql_command,(title,))
    results = cursor.fetchall()
    return results

def getAllFilmsTarantino(director):
    sql_command = """
        SELECT DISTINCT title
        FROM film
        WHERE director = ?

        """
    cursor.execute(sql_command,(director,))
    results = cursor.fetchall()
    return results

def getAllFilms(director):
    sql_command = """
        SELECT DISTINCT title
        FROM film
        WHERE director != ?

        """
    cursor.execute(sql_command,(director,))
    results = cursor.fetchall()
    return results