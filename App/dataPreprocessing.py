'''
@author Nicolas Ruth, Julian Fuchs
(c) 2019

Preprocesses the data pulled from the database via dbRetrieve in a way the connected tools f.ex.
d3 or plotly can process it easily.
'''

import networkx as nx
from networkx.readwrite import json_graph
from App import dbRetrieve
import json
import plotly
import plotly.graph_objs as go


def createGraph(title):
    '''
    Creates the networkx graph out of the data pulled from the database via dbRetrieve.py
    :param title:   The film title
    :return:        graphJson The networkx graph converted to json to be easly read by d3.js
    '''
    listOfEdges = dbRetrieve.getEdges(title)
    G = nx.Graph()
    G.add_weighted_edges_from(listOfEdges)
    graphJson = json_graph.node_link_data(G)
    return graphJson

def printableGraph(G):
    '''
    Not used anymore. Dead code, needs to be fixed.
    :param G:
    :return:
    '''
    data = json_graph.node_link_data(G)
    return data


def createPlot(character,info,chartType,title):
    '''
    Knowing the name of the character, the type of information (f.ex. topicMod) wanted,
    the charType (bar,pie) which should be produced and the film title this function pulls
    "label and value" - data through dbRetrieve.getLabelsAndValuesChart(character,info,title)
    and creates a plotly chart out of them.
    :param character:   name of the character the data is wanted of
    :param info:        which kind of information is wanted (topic modeling, psycholingo, archetype)
    :param chartType:   which chart type is wanted (bar, pie)
    :param title:       film title
    :return:            encoded plotly data in json format
    '''
    request = dbRetrieve.getLabelsAndValuesChart(character,info,title)
    labels = []
    values = []

    for i in request:
        labels.append(i[0])
        values.append(i[1])

    if(chartType == "bar"):
        data = go.Bar(x=labels,y=values)
    elif(chartType == "pie"):

        data = go.Pie(labels=labels,values=values)
    else:
        print("No valid chart format.")


    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def createPlotNetworkResults(algorithm,title,chartType):
    '''
    This function pulls data concerning the graph algorithms and creates an output
    readable with plotly.
    :param algorithm:   Specifies algorithm the data is wanted of
    :param title:       film title
    :param chartType:   which chart type is wanted (bar, pie)
    :return:            encoded plotly data in json format
    '''
    request = dbRetrieve.getLabelsAndValuesNetwork(algorithm,title)
    labels = []
    values = []

    for i in request:
        labels.append(i[0])
        values.append(i[1])

    if(chartType == "bar"):
        data = go.Bar(x=labels,y=values)
    elif(chartType == "pie"):

        data = go.Pie(labels=labels,values=values)
    else:
        print("No valid chart format.")

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def getText(character,title):
    '''
    Gets the spoken text of the character as written in the film script.
    :param character:   name of the character
    :param title:       film title
    :return:            text as string
    '''
    text = dbRetrieve.getText(character,title)
    text = str(text).replace("[","").replace("]","").replace("(","").replace(")","")
    text = text.replace("'","").replace(",","")

    return text

def getNetworkResults(title,algorithm):
    return dbRetrieve.getNwResults(title,algorithm)

def getAllCharacters(title):
    return dbRetrieve.getAllCharacters(title)

def getAllFilmsTarantino(director):
    return dbRetrieve.getAllFilmsTarantino(director)

def getAllFilms(director):
    return dbRetrieve.getAllFilms(director)