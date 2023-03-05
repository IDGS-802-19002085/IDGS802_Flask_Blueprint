import flask
 
from alumnos.routes import alumnos
from Directivos.routes import directivos
from Maestros.routes import maestros


app=flask.Flask(__name__)
app.config['DEBUG']=True


@app.route("/", method=[ "GET"])
def home():

    return flask.jsonfy({'principal':HOME})

app.register_blueprint(alumnos)
app.register_blueprint(dir)
app.register_blueprint(maestros)


if __name__='__name__':
    app.run()