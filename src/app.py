from flask import Flask
from flask import render_template, request,redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST']= 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD']= 'root'
app.config['MYSQL_DATABASE_DB']= 'empleados'

mysql.init_app(app) #inicializo la instancia

#Pruebo la conexion de la base de datos

@app.route('/')#decoradores de flask
def index():
    conn = mysql.connect()
    cursor= conn.cursor()
    
    sql = "SELECT * FROM empleados;"
    cursor.execute(sql)
    
    emplados = cursor. fetchall()
    
    conn.commit()
    
    return render_template('empleados/index.html', 
    empleados = empleados)
    
        
@app.route('/create')
def create():
   return render_template('empleados/create.html')
   
   
@app.route('/store', methods=["POST"])
def store(): 
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.fiel['txtFoto']

    sql = "INSERT INTO empleados(nombre, correo, foto) values (%s, %s, %s);"#s va porque son String
    datos = (_nombre, _correo, _foto.fielname)

    conn = mysql.connect()
    cursor= conn.cursor()
    cursor.execute(sql, datos) 
    conn.commit()#aca se guarda en el base de datos
    
    return redirect('/')
    


   
   
   

if __name__== '__main__':
    app.run(debug=True)
