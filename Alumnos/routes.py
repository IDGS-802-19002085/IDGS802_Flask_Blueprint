from flask blueprint


alumnos=Blueprints('alumnos', __name__)

@alumnos.route('/gealum',methods=[ "GET"])
def getalum():
    return {'key':'Alumnos'}
