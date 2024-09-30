from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operador = int(request.form['oper-s'] or request.form['oper-r'] or request.form['oper-m'] or request.form['oper-d'])

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

        return render_template('index.html', resultado=resultado, operacion=operacion, num1=num1, num2=num2)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    