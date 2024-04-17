from flask import Flask, render_template, request

def par(w):
    cont=0 
    for cada in w:
        if cada % 2 == 0:
            cont += 1
        
    return cont

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Recebe os números fornecidos pelo usuário do formulário
    numbers_input = request.form['numbers']
    # Converte a string de entrada em uma lista de números inteiros
    numbers = [int(num) for num in numbers_input.split(',')]

    # Calcula o número total de números pares usando a lógica do código anterior
    total_pares = par(numbers)
    
    # Retorna o número total de números pares
    return f'Há {total_pares} números pares.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
