from flask Blueprint


maestros=Blueprints('maestros', __name__)

@alumnos.route('/getMaes',methods=[ "GET"])
def getalum():
    return {'key':'maestros'}