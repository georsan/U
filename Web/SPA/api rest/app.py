from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
 
app = Flask(__name__)
#conecion con mysql
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://georsan:2182028@localhost/web'
#para que no de error
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
CORS(app, supports_credentials=True)
#pasar config al orm
db= SQLAlchemy(app)
#esquema
mar= Marshmallow(app)

#creando en la base de datos

#clase tipo doc
class tip_doc(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    nombre=db.Column(db.String(60))
    descripcion=db.Column(db.String(60))

#contrutor
    def __init__(self,nombre,descripcion):
        self.nombre=nombre
        self.descripcion=descripcion    

#crear en mysql
db.create_all()

#instanciar


#tabla ciudad

class ciudadx(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    ciudad=db.Column(db.String(60))
    departamento=db.Column(db.String(60))
    
#contrutor
    def __init__(self,ciudad,departamento):
        self.ciudad=ciudad
        self.departamento=departamento  
            

#crear en mysql
db.create_all()
 
#tabla persona
class persona(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    nombre=db.Column(db.String(60))
    apellidos=db.Column(db.String(60))
    idtipodoc=db.Column(db.ForeignKey('tip_doc.id'))
    documento=db.Column(db.Integer)
    idtipociu=db.Column(db.ForeignKey('ciudadx.id'))
    fechanacimiento=db.Column(db.String(60))
    email=db.Column(db.String(60))
    telefono=db.Column(db.Integer)
    usuario=db.Column(db.String(60))
    password=db.Column(db.String(60))
    
#construtor
    def __init__(self,nombre,apellidos,idtipodoc,documento,idtipociu,fechanacimiento,email,telefono,usuario,password):
        self.nombre=nombre
        self.apellidos=apellidos
        self.idtipodoc=idtipodoc
        self.documento=documento
        self.idtipociu=idtipociu
        self.fechanacimiento=fechanacimiento
        self.email=email
        self.telefono=telefono
        self.usuario=usuario
        self.password=password

#crear en mysql
db.create_all()
 
 #crear esquema
class Xdchema(mar.Schema):
    class Meta:
        fields=('id', 'nombre', 'descripcion','ciudad','departamento','apellidos','documento','idtipociu')

#instanciar
uno = Xdchema()
#obtener muchos
muchos= Xdchema(many=True)












#ruta para crear

#crear documento
@app.route('/document',methods=['POST'])

def crear_documento():

    nombre = request.json['nombre']
    
    descripcion = request.json['descripcion']
    
    nea = tip_doc(nombre,descripcion)    

    db.session.add(tip_doc(nombre,descripcion))

    db.session.commit() 

    return uno.jsonify(nea)
    
#ciudad
@app.route('/ciudades',methods=['POST'])

@cross_origin()

def crear_ciudades():

    ciudad = request.json['ciudad']

    departamento=request.json['departamento']

    nea = ciudadx(ciudad,departamento)    

  
    db.session.add(ciudadx(ciudad,departamento))

    db.session.commit() 
    

    return uno.jsonify(nea)

#persona
@app.route('/persona',methods=['POST'])

@cross_origin()

def crear_persona():

    nombre = request.json['nombre']

    apellidos=request.json['apellidos']

    idtipodoc=request.json['idtipodoc']

    documento= request.json['documento']

    idtipociu=request.json['idtipociu']
    
    fechanacimiento=request.json['fechanacimiento']
    
    email=request.json['email']
    
    telefono=request.json['telefono']
    
    usuario=request.json['usuario']
    
    password=request.json['password']

    nea = persona(nombre,apellidos,idtipodoc,documento,idtipociu,fechanacimiento,email,telefono,usuario,password)

    db.session.add(persona(nombre,apellidos,idtipodoc,documento,idtipociu,fechanacimiento,email,telefono,usuario,password))


    db.session.commit() 
    

    return uno.jsonify(nea)


#colsutando de la bd
#obteniendo tipo documentos
@app.route('/document',methods=['GET'])

@cross_origin()

def obtener_docs():
    alldocumet = tip_doc.query.all()

    document = muchos.dump(alldocumet)

    return jsonify(document )

#obteniendo tipo ciudad
@app.route('/ciudades',methods=['GET'])

@cross_origin()

def obtener_ciudad():

    allciudad = ciudadx.query.all()

    ciudades = muchos.dump(allciudad)

    return jsonify(ciudades )
#obteniendo persona
@app.route('/persona',methods=['GET'])

@cross_origin()

def obtener_persona():

    allpersona = persona.query.all()

    personas = muchos.dump(allpersona)

    return jsonify(personas )

#obtener una solo dato

#obtener documento

@app.route('/document/<id>',methods=['GET'])

@cross_origin()

def obtener_doc(id):
    
    docu=tip_doc.query.get(id)

    return  uno.jsonify(docu)

#obtener ciudad

@app.route('/ciudades/<id>',methods=['GET'])

@cross_origin()

def obtener_ciu(id):
    
    ciu=ciudadx.query.get(id)

    return  uno.jsonify(ciu)

#obtener documento

@app.route('/persona/<id>',methods=['GET'])

@cross_origin()

def obtener_person(id):
    
    per=persona.query.get(id)

    return  uno.jsonify(per)


# editar

#editar documento

@app.route('/document/<id>',methods=['PUT'])

@cross_origin()

def updatedoc(id):
    
    editdocu=tip_doc.query.get(id)

    nombre= request.json['nombre']

    descripcion = request.json['descripcion']

    editdocu.nombre=nombre

    editdocu.descripcion=descripcion
    
    db.session.commit()

    return  uno.jsonify(editdocu)

    #editar ciudad

@app.route('/ciudades/<id>',methods=['PUT'])
@cross_origin(supports_credentials=True)
def updateciu(id):
    
    editciu=ciudadx.query.get(id)

    ciudad= request.json['ciudad']

    departamento = request.json['departamento']

    editciu.ciudad=ciudad

    editciu.departamento=departamento
    
    db.session.commit()

    return  uno.jsonify(editciu)

  #editar persona

@app.route('/persona/<id>',methods=['PUT'])

@cross_origin()

def updateper(id):
    
    editper=persona.query.get(id)
    
    nombre = request.json['nombre']
    
    apellidos=request.json['apellidos']
    
    idtipodoc=request.json['idtipodoc']
    
    documento= request.json['documento']
    
    idtipociu=request.json['idtipociu']
    
    fechanacimiento=request.json['fechanacimiento']
    
    email=request.json['email']
    
    telefono=request.json['telefono']
    
    usuario=request.json['usuario']
    
    password=request.json['password']

   
    editper.nombre=nombre

    editper.apellidos=apellidos

    editper.idtipodoc=idtipodoc

    editper.documento=documento

    editper.idtipociu=idtipociu

    editper.fechanacimiento=fechanacimiento

    editper.email=email

    editper.telefono=telefono

    editper.usuario=usuario

    editper.password=password
    
    db.session.commit()
    
    return uno.jsonify(editper)


#eliminar

#eliminar documetos

@app.route('/document/<id>',methods=['DELETE'])

@cross_origin()

def deletedoc(id):
    
    deldocu=tip_doc.query.get(id)

    db.session.delete(deldocu)

    db.session.commit()

    return  uno.jsonify(deldocu)

#eliminar ciudad

@app.route('/ciudades/<id>',methods=['DELETE'])

@cross_origin(supports_credentials=True)

def deleteciu(id):
    
    delciu=ciudadx.query.get(id)

    db.session.delete(delciu)

    db.session.commit()

    return  uno.jsonify(delciu)


#eliminar persona

@app.route('/persona/<id>',methods=['DELETE'])

@cross_origin()

def deleteper(id):
    
    delper=persona.query.get(id)

    db.session.delete(delper)

    db.session.commit()

    return  uno.jsonify(delper)












#levantar servidor
if  __name__ == '__main__':
    app.run(debug=True)

