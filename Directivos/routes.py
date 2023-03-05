from flask Blueprint


directivos=Blueprints('dir', __name__)

@alumnos.route('/getDir',methods=[ "GET"])
def getalum():
    return {'key':'Directivos'}