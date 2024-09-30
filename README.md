# Act4-ADS
En este repositorio depositaré los archivos de la Actividad4 de  Arquitectura de Software
#En este ejercicio he creado una "calculadora" básica que nos permita realizar las 4 operaciones básicas entre dos números, 
# el usuario nos proveera el operador matematico y los dos numeros a operar. 
# Vamos a enlazar la interfaz del usuario
#  
# Importamos las libreria Flask que nos permitira ver la maquetación en html e interactuar con ella.

from flask import Flask, render_template, request

app = Flask(__name__)
#Creamos la ruta de nuestra visual web

@app.route('/', methods=['GET', 'POST'])
#Definimos la Función Index que nos ayudara a solicitar la información desde el html
def index():
    #Definimos el metodo que usaremos para traer la informacion
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operador = int(request.form['oper-s'] or request.form['oper-r'] or request.form['oper-m'] or request.form['oper-d'])

#Definimos las operaciones a realizar , el resultado y el tipo de operacion
        if operador == 1:
            resultado = num1 + num2
            operacion = "Suma"
        elif operador == 2:
            resultado = num1 - num2
            operacion = "Resta"
        elif operador == 3:
            resultado = num1 * num2
            operacion = "Multiplicación"
        elif operador == 4:
            if num2 != 0:
                resultado = num1 / num2
                operacion = "División"
            else:
                resultado = "Error: División por cero"
#Pedimos que nos retorne la vista y las nuevas variables
        return render_template('index.html', resultado=resultado, operacion=operacion, num1=num1, num2=num2)
    return render_template('index.html')
#Definimos la funcionalidad del archivo

if __name__ == "__main__":
    app.run(debug=True)
    
