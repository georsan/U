from flask import Flask,render_template,request,redirect,url_for,session,flash
from flask_mysqldb import MySQL

#-------------------------------
app= Flask(__name__)

#clave secreta
app.secret_key='12345'

app.static_folder = 'static'

#conxion mysql
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'georsan'
app.config['MYSQL_PASSWORD']= '2182028'
app.config['MYSQL_DB']= 'school'

#declarar variable mysql
mysql= MySQL(app)

#ruta principal
@app.route('/')

def main():
    if 'nombre' in session:
        return render_template('Login.html')
    else:
        return render_template('Login.html')


@app.route('/inicio')

def inicio():
    if 'nombre' in session:
        return render_template('Login.html')
    else:
        return render_template('Login.html')

 
@app.route('/ingresar',methods=['GET','POST'])

def ingresar():
    if request.method=='GET':
        if 'nombre' in session:
            return render_template('Login.html')
        else:
            return render_template('Login.html')

    else:
        user = request.form['usuario']
        passw= request.form['contrasena']

        cur = mysql.connection.cursor()

        sQuery= 'SELECT usuario,contraseña,rol FROM usuario WHERE usuario=%s'

        cur.execute(sQuery,[user]) 

        usuario=cur.fetchone()

        cur.close

        if user !=None:
            
            if passw != usuario[1]:
                flash('Clave incorrecta','alert-warning')
                return redirect(url_for('inicio'))
            else:
                if usuario[2]==1:
                    session['nombre']=usuario[0]                
                    return render_template('index.html')
                elif usuario[2]==2:
                    session['nombre']=usuario[0]
                    return redirect(url_for('Ver_stuedent'))
                else:
                    session['nombre']=usuario[0]
                    return 'aqui va estudiante'     
        else:
            flash('Usuario no encontrado')
            
@app.route('/in')

def ini():

    return render_template('index.html')


@app.route('/salir')

def salir():
    session.clear()
    return redirect(url_for('ingresar'))




##################################################################
#admin

#estudiante crud
@app.route('/Estudiante_look')

def Ver_estudiante():

    cur = mysql.connection.cursor()

    cur.execute('SELECT id_estudiante,codigo,nombre,apellido, tipo_documento,documento,correo,telefono,usuario FROM estudiante;')
    
    student=cur.fetchall()
    
    cur.close()

    return render_template('Estudiante.html',estudian=student)  
    

@app.route('/Estudiante_add',methods=['GET','POST'])

def add_estudiante():

    if request.method=='GET':
        return render_template('addEstudiante.html')
    
    else:
        nomb=request.form['nombre']

        apell=request.form['apellido']

        tip= request.form['tipo']

        docu = request.form['documento']

        em = request.form['email']

        tel = request.form['telefono']

        cur = mysql.connection.cursor()

        user = request.form['usuario']

        cur.execute('INSERT INTO estudiante (nombre,apellido,tipo_documento,documento,correo,telefono) VALUES (%s,%s,%s,%s,%s,%s)',(nomb,apell,tip,docu,em,tel))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_estudiante'))
    return render_template('addEstudiante.html')

@app.route('/Estudiante_edit/<id>',methods=['GET','POST'])
def editar_estudiante(id):
    cur=mysql.connection.cursor()

    cur.execute('select id_estudiante,nombre,apellido,tipo_documento,documento,correo,telefono FROM estudiante WHERE id_estudiante=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editEstudiante.html',editar=edi[0])
@app.route('/uptdate/<id>',methods=['GET','POST'])
def uptdate(id):
    if request.method=='POST': 
        nomb=request.form['nombre']

        apell=request.form['apellido']

        tip= request.form['tipo']

        docu = request.form['documento']

        em = request.form['email']

        tel = request.form['telefono']

    
        cur= mysql.connection.cursor()

        cur.execute('UPDATE estudiante SET nombre=%s,apellido=%s,tipo_documento=%s,documento=%s,correo=%s,telefono=%s where id_estudiante=%s',(nomb,apell,tip,docu,em,tel,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_estudiante'))

@app.route('/delete/<id>',methods=['GET','POST'])
def delete_est(id):
     cur = mysql.connection.cursor()
     cur.execute('DELETE from estudiante where id_estudiante=%s',(id,))
     mysql.connection.commit()
     cur.close()
     return redirect(url_for('Ver_estudiante'))

#CRUD PROFESOR
@app.route('/Profesor_look')

def Ver_Profesor():

    cur = mysql.connection.cursor()

    cur.execute('SELECT id_profesor,codigo,nombre,apellido,cedula,correo,telefono,usuario.usuario,usuario.contraseña FROM profesor,usuario where profesor.usuario=usuario.id_usuario;')
    
    profe=cur.fetchall()
    
    cur.close()

    return render_template('Profesor.html',Profesor=profe)  
    

@app.route('/Profesor_add',methods=['GET','POST'])

def add_Profesor():

    if request.method=='GET':
        return render_template('addProfesor.html')
    
    else:
        nomb=request.form['nombre']

        apell=request.form['apellido']

        docu = request.form['documento']

        em = request.form['email']

        tel = request.form['telefono']

        user = request.form['usuario']

        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO profesor(nombre,apellido,cedula,correo,telefono,usuario) VALUES (%s,%s,%s,%s,%s,%s)',(nomb,apell,docu,em,tel,user))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_Profesor'))
    return render_template('addPofesor.html')

@app.route('/Profesor_edit/<id>',methods=['GET','POST'])
def editar_profe(id):
    cur=mysql.connection.cursor()

    cur.execute('select id_profesor,nombre,apellido,cedula,correo,telefono FROM profesor WHERE id_profesor=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editProfesor.html',editar=edi[0])

@app.route('/uptdate_Pro/<id>',methods=['GET','POST'])
def uptdatepro(id):
    if request.method=='POST': 
        nomb=request.form['nombre']

        apell=request.form['apellido']

        docu = request.form['documento']

        em = request.form['email']

        tel = request.form['telefono']

    
        cur= mysql.connection.cursor()

        cur.execute('UPDATE profesor SET nombre=%s,apellido=%s,cedula=%s,correo=%s,telefono=%s where id_profesor=%s',(nomb,apell,docu,em,tel,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_Profesor'))

@app.route('/delete_profe/<id>',methods=['GET','POST'])
def delete_pro(id):
     cur = mysql.connection.cursor()
     cur.execute('DELETE from profesor where id_profesor=%s',(id,))
     mysql.connection.commit()
     cur.close()
     return redirect(url_for('Ver_Profesor'))

#CRUD Materia
@app.route('/Materia_look')

def Ver_Materia():

    cur = mysql.connection.cursor()

    cur.execute('SELECT *FROM materia;')
    
    materia=cur.fetchall()
    
    cur.close()

    return render_template('materia.html',materias=materia)  

@app.route('/Materia_add',methods=['GET','POST'])

def add_Mareria():

    if request.method=='GET':
        return render_template('addmateria.html')
    
    else:        
        id=request.form['id']

        nomb=request.form['nombre']

        apell=request.form['horario']

        id=request.form['id']

        nomb=request.form['nombre']

        apell=request.form['horario']

        cur= mysql.connection.cursor()
        
        cur.execute('INSERT INTO materia(id_materia,nombre,horario) VALUES (%s,%s,%s)',(id,nomb,apell))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_Materia'))
    return render_template('addmateria.html')


@app.route('/Materia_edit/<id>',methods=['GET','POST'])
def editar_materia(id):
    cur=mysql.connection.cursor()

    cur.execute('select *FROM materia WHERE id_materia=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editarmateria.html',editar=edi[0])


@app.route('/uptdate_mate/<id>',methods=['GET','POST'])
def uptdatemate(id):
    if request.method=='POST': 
        id_x=request.form['id']

        nomb=request.form['nombre']

        apell=request.form['horario']

    
        cur= mysql.connection.cursor()

        cur.execute('UPDATE materia SET id_materia=%s,nombre=%s,horario=%s where id_materia=%s',(id_x,nomb,apell,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_Materia'))

@app.route('/delete_mate/<id>',methods=['GET','POST'])
def delete_materia(id):
     cur = mysql.connection.cursor()
     cur.execute('DELETE from materia where id_materia=%s',(id,))
     mysql.connection.commit()
     cur.close()
     return redirect(url_for('Ver_Materia'))

########################################################3
#grado
#CRUD Materia
@app.route('/Grado_look')

def Ver_Grado():

    cur = mysql.connection.cursor()

    cur.execute('SELECT *FROM grado;')
    
    grado=cur.fetchall()
    
    cur.close()

    return render_template('grado.html',grados=grado)

@app.route('/Grado_add',methods=['GET','POST'])

def add_Grado():

    if request.method=='GET':
        return render_template('addgrado.html')
    
    else:
        id_g = request.form['grado']
       
        nomb=request.form['nombre']
       
        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO grado(id_grado,nombre) VALUES (%s,%s)',(id_g,nomb))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_Grado'))
    return render_template('addgrado.html')

@app.route('/Grado_edit/<id>',methods=['GET','POST'])
def editar_grado(id):
    cur=mysql.connection.cursor()

    cur.execute('select  *FROM grado WHERE id_grado=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editgrado.html',editar=edi[0])

@app.route('/uptdate_grado/<id>',methods=['GET','POST'])
def uptdategra(id):
    if request.method=='POST': 
       
        nomb=request.form['nombre']

        id_g=request.form['grado']

        cur= mysql.connection.cursor()

        cur.execute('UPDATE grado SET id_grado=%s,nombre=%s where id_grado=%s',(id_g,nomb,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_Grado'))

@app.route('/delete_grado/<id>',methods=['GET','POST'])
def delete_grado(id):
     cur = mysql.connection.cursor()
     cur.execute('DELETE from grado where id_grado=%s',(id,))
     mysql.connection.commit()
     cur.close()
     return redirect(url_for('Ver_Grado'))

###########################################
@app.route('/aula_look')

def Ver_aula():

    cur = mysql.connection.cursor()

    cur.execute('SELECT *FROM aula;')
    
    aula=cur.fetchall()
    
    cur.close()

    return render_template('aula.html',aulas=aula)

@app.route('/Aula_add',methods=['GET','POST'])

def add_aula():

    if request.method=='GET':
        return render_template('addaula.html')
    
    else:
        id_g = request.form['id_aula']
       
        nomb=request.form['numero']

        cap=request.form['capacidad']

        grado=request.form['grado']
       
        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO aula(id_aula,numero,capacidad,grado) VALUES (%s,%s,%s,%s)',(id_g,nomb,cap,grado))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_aula'))
    return render_template('addaula.html')

@app.route('/Aula_edit/<id>',methods=['GET','POST'])
def editar_aula(id):
    cur=mysql.connection.cursor()

    cur.execute('select  *FROM aula WHERE id_aula=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editaula.html',editar=edi[0])

@app.route('/uptdate_aula/<id>',methods=['GET','POST'])
def uptdateaul(id):
    if request.method=='POST': 

        id_g = request.form['aula']
       
        nomb=request.form['nombre']

        cap=request.form['capacidad']

        cur= mysql.connection.cursor()

        cur.execute('UPDATE aula SET id_aula=%s,numero=%s,capacidad=%s where id_aula=%s',(id_g,nomb,cap,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_aula'))

@app.route('/delete_aula/<id>',methods=['GET','POST'])
def delete_aula(id):
     cur = mysql.connection.cursor()
     cur.execute('DELETE from aula where id_aula=%s',(id,))
     mysql.connection.commit()
     cur.close()
     return redirect(url_for('Ver_aula'))

#########################################################

@app.route('/Estudiante-grado')

def Ver_eg():

    cur = mysql.connection.cursor()

    cur.execute('SELECT *FROM estudiante_grado;')
    
    e_g=cur.fetchall()
    
    cur.close()

    #return render_template('estudiante-grado.html')

    cursor = mysql.connection.cursor()

    cursor.execute('SELECT *FROM profesor_materia;')
    
    est=cursor.fetchall()
    
    cursor.close()

    return render_template('estudiante-grado.html',profe=est,esg=e_g)




@app.route('/eg_add',methods=['GET','POST'])

def add_eg():

    if request.method=='GET':
        return render_template('addestudiante-grado.html')
    
    else:
        id_g = request.form['grado']
       
        nomb=request.form['estudiante']
       
        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO estudiante_grado(estudiante,grado) VALUES (%s,%s)',(nomb,id_g))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_eg'))
    return render_template('addestudiante-grado.html')




@app.route('/eg_edit/<id>',methods=['GET','POST'])
def eg(id):
    cur=mysql.connection.cursor()

    cur.execute('select  *FROM estudiante_grado WHERE estudiante=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editestudiante-grado.html',editar=edi[0])

@app.route('/uptdate_eg/<id>',methods=['GET','POST'])
def uptdateeg(id):
    if request.method=='POST': 

        id_g = request.form['estudiante']
       
        nomb=request.form['grado']

        

        cur= mysql.connection.cursor()

        cur.execute('UPDATE estudiante_grado SET estudiante=%s,grado=%s where estudiante=%s',(id_g,nomb,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_eg'))


@app.route('/delete_eg/<id>',methods=['GET','POST'])

def delete_eg(id):
     cur = mysql.connection.cursor()
     cur.execute('DELETE from estudiante_grado where estudiante=%s',(id,))
     mysql.connection.commit()
     cur.close()
     return redirect(url_for('Ver_eg'))
#########################################################3


@app.route('/pm_add',methods=['GET','POST'])

def add_pm():

    if request.method=='GET':
        return render_template('addprofesor-materia.html')
    
    else:
        profesor = request.form['profesor']
       
        materia=request.form['materia']
       
        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO profesor_materia(profesor,materia) VALUES (%s,%s)',(profesor,materia))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_eg'))
    return render_template('addprofesor-materia.html')




@app.route('/pm_edit/<id>',methods=['GET','POST'])
def pm(id):
    cur=mysql.connection.cursor()

    cur.execute('select  *FROM profesor_materia WHERE id=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editprofesor-materia.html',editar=edi[0])

@app.route('/uptdate_pm/<id>',methods=['GET','POST'])
def uptdatepm(id):
    if request.method=='POST': 

        profesor = request.form['profesor']
       
        materia=request.form['materia']
        

        cur= mysql.connection.cursor()

        cur.execute('UPDATE profesor_materia SET profesor=%s,materia=%s where id=%s',(profesor,materia,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_eg'))


@app.route('/delete_pm/<id>',methods=['GET','POST'])

def delete_pm(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE from profesor_materia where id=%s',(id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('Ver_eg'))














##########################################################################################################


@app.route('/Periodo')

def Ver_peridod():

    cur = mysql.connection.cursor()

    cur.execute('SELECT *FROM periodo;')
    
    per=cur.fetchall()
    
    cur.close()

    return render_template('periodo.html',periodos=per)


@app.route('/periodo_add',methods=['GET','POST'])

def add_peridod():

    if request.method=='GET':
        return render_template('addperiodo.html')
    
    else:
        id_g = request.form['periodo']
       
        nomb=request.form['fecha']

        num=request.form['numero']
       
        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO periodo(id_periodo,fecha,numero) VALUES (%s,%s,%s)',(id_g,nomb,num))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_peridod'))
    return render_template('addperiodo.html')




@app.route('/periodo_edit/<id>',methods=['GET','POST'])
def perido(id):
    cur=mysql.connection.cursor()

    cur.execute('select  *FROM periodo WHERE id_periodo=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editarperiodo.html',editar=edi[0])

@app.route('/uptdate_perido/<id>',methods=['GET','POST'])
def uptdateprido(id):
    if request.method=='POST': 

       
        nomb=request.form['fecha']

        xd=request.form['numero']

        

        cur= mysql.connection.cursor()

        cur.execute('UPDATE periodo SET fecha=%s,numero=%s where id_periodo=%s',(nomb,xd,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_peridod'))


@app.route('/delete_perido/<id>',methods=['GET','POST'])
def delete_perido(id):
     cur = mysql.connection.cursor()
     cur.execute('DELETE from periodo where id_periodo=%s',(id,))
     mysql.connection.commit()
     cur.close()
     return redirect(url_for('Ver_peridod'))

####################################################################

@app.route('/actividad/<id>')

def Ver_acrividad(id):

    cur = mysql.connection.cursor()

    cur.execute('SELECT  actividad.id_actividad,actividad.nombre,actividad.fecha_entrega FROM actividad_materia,materia,actividad where  actividad_materia.materia=materia.id_materia and actividad_materia.actividad=id_actividad and materia.id_materia=%s',(id,))
    
    act=cur.fetchall()
    
    cur.close()

    

    return render_template('actividad.html',activ=act,xds=id)


@app.route('/actividad_add/<id>',methods=['GET','POST'])

def add_actividad(id):

    if request.method=='GET':
        return render_template('addactividad.html')
    
    else:
        id_actividad = request.form['id_actividad']
       
        nombre=request.form['nombre']


        fecha_entrega=request.form['fecha_entrega']
       
        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO actividad(id_actividad,nombre,fecha_entrega) VALUES (%s,%s,%s)',(id_actividad,nombre,fecha_entrega))

        mysql.connection.commit()

        cur.close()

        curs=mysql.connection.cursor()

        curs.execute('INSERT INTO  actividad_materia (actividad,materia) values (%s,%s)',(id_actividad,id))

        mysql.connection.commit()

        curs.close()
        
        return redirect(url_for('Ver_stuedent'))
    return render_template('addactividad.html')




@app.route('/actividad_edit/<id>',methods=['GET','POST'])
def editactiviadad(id):
    cur=mysql.connection.cursor()

    cur.execute('select id_actividad,nombre,fecha_entrega  FROM actividad WHERE id_actividad=%s',(id,) )

    edi = cur.fetchall()

    return render_template('editactividad.html',editar=edi[0])

@app.route('/uptdate_actividad/<id>',methods=['GET','POST'])
def uptdateactividad(id):
    if request.method=='POST': 

        
       
        nombre=request.form['nombre']

        fecha_entrega=request.form['fecha_entrega']

        cur= mysql.connection.cursor()

        cur.execute('UPDATE actividad SET nombre=%s,fecha_entrega=%s where id_actividad =%s',(nombre,fecha_entrega,id))

        mysql.connection.commit()

        cur.close()
        return redirect(url_for('Ver_stuedent'))


@app.route('/delete_actividad/<id>',methods=['GET','POST'])
def delete_act(id):

     cur2 = mysql.connection.cursor()
     cur2.execute('DELETE FROM actividad_materia where actividad=%s',(id,))
     mysql.connection.commit()
     cur2.close()


     cur = mysql.connection.cursor()
     cur.execute('DELETE from actividad where id_actividad=%s',(id,))
     mysql.connection.commit()
     cur.close()
     return redirect(url_for('Ver_stuedent'))


##############################################################33

@app.route('/calificar/<id>')

def Ver_calif(id):

    cur = mysql.connection.cursor()

    cur.execute('SELECT materia.id_materia,calificacion.id_calificacion, calificacion.nombre,calificacion.numero,calificacion.periodo FROM materia_calificacion,calificacion,materia where materia_calificacion.materia=materia.id_materia and materia_calificacion.calificacion=calificacion.id_calificacion and materia_calificacion.materia=%s',(id,))
    
    calificacion=cur.fetchall()
    
    cur.close()
    
    return render_template('Calificacion.html',calificaciones=calificacion,xd=id)


@app.route('/calificacion_add/<id>',methods=['GET','POST'])

def add_calf(id):
    
    if request.method=='GET':
        return render_template('addcalificacion.html')
    
    else:
        id_calificacion = request.form['id_calificacion']
       
        nombre=request.form['nombre']


        numero=request.form['numero']

        periodo=request.form['periodo']
       
        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO calificacion(id_calificacion,nombre,numero,periodo) VALUES (%s,%s,%s,%s)',(id_calificacion,nombre,numero,periodo))

        mysql.connection.commit()

        cur.close()

        curs = mysql.connection.cursor()

        curs.execute('INSERT into materia_calificacion(materia,calificacion) values(%s,%s)',(id,id_calificacion))
        
        mysql.connection.commit()

        curs.close()
        
        return redirect(url_for('Ver_stuedent'))
    return render_template('addcalificacion.html')




#@app.route('/calificacion_edit/<id>',methods=['GET','POST'])
#def editacalificacion(id):
#   cur=mysql.connection.cursor()

#    cur.execute('select  *FROM actividad WHERE id_actividad=%s',(id,) )

#    edi = cur.fetchall()

 #   return render_template('editactividad.html',editar=edi[0])

#@app.route('/uptdate_actividad/<id>',methods=['GET','POST'])
#def uptdateactividad(id):
#    if request.method=='POST': 

        
       
#        nombre=request.form['nombre']

#        fecha_entrega=request.form['fecha_entrega']

#        cur= mysql.connection.cursor()

#        cur.execute('UPDATE actividad SET nombre=%s,fecha_entrega=%s where id_actividad =%s',(nombre,fecha_entrega,id))

#        mysql.connection.commit()

#        cur.close()
#        return redirect(url_for('Ver_acrividad'))


@app.route('/delete_calificacion/<id>',methods=['GET','POST'])
def delete_calf(id):

     cur1 = mysql.connection.cursor()
     cur1.execute('DELETE FROM materia_calificacion where calificacion=%s',(id,))
     mysql.connection.commit()
     cur1.close()



     cur = mysql.connection.cursor()
     cur.execute('DELETE from calificacion where id_calificacion=%s',(id,))
     mysql.connection.commit()
     cur.close()



     return redirect(url_for('Ver_stuedent'))














##################################################################3

@app.route('/ver')

def Ver_stuedent():
                
    print(session)

    cur = mysql.connection.cursor()

    cur.execute('SELECT materia.id_materia,materia.nombre,materia.horario FROM profesor_materia,materia,profesor where materia.id_materia=profesor_materia.materia and profesor.id_profesor=profesor_materia.profesor')
    
    student=cur.fetchall()
    
    cur.close()

    return render_template('Profesorview.html',materias=student)



























#levantar servidor
if __name__=='__main__':
    app.run(debug=True)