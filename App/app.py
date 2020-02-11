'''
@author Nicolas Ruth, Julian Fuchs
(c) 2019
'''

from flask import Flask, render_template, request
from App import dataPreprocessing

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/tarantino", methods=['GET', 'POST'])
def tarantino():
    '''
    Create the page concerning the analysis of the tarantino films.
    :return:
    '''

    title = ""
    #dropdown menue input
    title = request.form.get('comp_select')
    director = "Tarantino"
    titles = dataPreprocessing.getAllFilmsTarantino(director)
    filmTitles = []
    for film in titles:
        filmTitles.append({"title": film[0]})

    #get the graph data as a json through dataPreprocessing
    graph = dataPreprocessing.createGraph(title)

    #get all characterNames of the chosen film
    characterNames = dataPreprocessing.getAllCharacters(title)

    #collect the data of all characters and append them to arrays
    names = []
    topics = []
    psychs = []
    archs = []
    texts = []
    for i in characterNames:
        character = i[0]
        text = dataPreprocessing.getText(character,title)
        topicModelling = dataPreprocessing.createPlot(character,"tpMod","pie",title)
        psychics = dataPreprocessing.createPlot(character, "psychics", "bar",title)
        archetypes = dataPreprocessing.createPlot(character, "archetyp", "bar",title)
        names.append(character)
        topics.append(topicModelling)
        psychs.append(psychics)
        archs.append(archetypes)
        texts.append(text)

    #get the values of the graph algorithms
    pagerank = dataPreprocessing.createPlotNetworkResults("pagerank",title,"bar")
    degreeC = dataPreprocessing.createPlotNetworkResults("degreeCentrality",title,"bar")
    closenessC = dataPreprocessing.createPlotNetworkResults("closenessCentrality",title,"bar")

    #put these values in an dictionary
    networkResults = {"Pagerank" : pagerank, "Degree Centrality" : degreeC, "Closeness Centrality": closenessC}

    #send all this data to the html page tarantino.html
    return render_template(
        "tarantino.html",
        data = graph,
        names = names,
        titles = filmTitles,
        networkResults = networkResults,
        plot = [],
        topicData = topics,
        psychData = psychs,
        archData = archs,
        texts = texts
    )


@app.route("/casestudy")
def casestudy():
    '''
    Create the page that only shows the research paper.
    :return:
    '''
    return render_template("casestudy.html")

@app.route("/continued")
def continued():
    '''
    Create the page that hints other directors are gonna to be added to the database.
    :return:
    '''
    return render_template("continued.html")

@app.route("/other", methods=['GET', 'POST'])
def other():
    '''
    Create the page that shows all other films in the database.
    :return:
    '''
    title = ""
    #dropdown menue input
    title = request.form.get('comp_select')
    director = "Tarantino"
    titles = dataPreprocessing.getAllFilms(director)
    filmTitles = []
    for film in titles:
        filmTitles.append({"title": film[0]})

    #get the graph data as a json through dataPreprocessing
    graph = dataPreprocessing.createGraph(title)

    #get all characterNames of the chosen film
    characterNames = dataPreprocessing.getAllCharacters(title)

    #collect the data of all characters and append them to arrays
    names = []
    topics = []
    psychs = []
    archs = []
    texts = []
    for i in characterNames:
        character = i[0]
        text = dataPreprocessing.getText(character, title)
        topicModelling = dataPreprocessing.createPlot(character, "tpMod", "pie", title)
        psychics = dataPreprocessing.createPlot(character, "psychics", "bar", title)
        archetypes = dataPreprocessing.createPlot(character, "archetyp", "bar", title)
        names.append(character)
        topics.append(topicModelling)
        psychs.append(psychics)
        archs.append(archetypes)
        texts.append(text)

    #get the values of the graph algorithms
    pagerank = dataPreprocessing.createPlotNetworkResults("pagerank", title, "bar")
    degreeC = dataPreprocessing.createPlotNetworkResults("degreeCentrality", title, "bar")
    closenessC = dataPreprocessing.createPlotNetworkResults("closenessCentrality", title, "bar")

    #put these values in an dictionary
    networkResults = {"Pagerank": pagerank, "Degree Centrality": degreeC, "Closeness Centrality": closenessC}

    #send all this data to the html page otherseries.html
    return render_template(
        "otherSeries.html",
        data=graph,
        names=names,
        titles=filmTitles,
        networkResults=networkResults,
        plot=[],
        topicData=topics,
        psychData=psychs,
        archData=archs,
        texts=texts
    )

#starting in an IDE without a run.py file
'''
if __name__ == "__main__":
    app.run(debug=True)
'''