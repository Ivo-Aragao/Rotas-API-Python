from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return redirect('/lista_produtos')

@app.route('/lista_produtos')
def lista_produtos():
    total = calcular_valor_total()
    return render_template('lista_produtos.html', tasks=tasks, total=total)

@app.route('/adicionar_produto', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        
        produto = {
            'id': len(tasks)+1,
            'nome': request.form['produto'],
            'quantidade': int(request.form['quantidade']),
            'preco': float(request.form['preco'])
        }
        tasks.append(produto)
        

        return redirect('/lista_produtos')
    return render_template('adicionar_produto.html')

@app.route('/editar-produto/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    for task in tasks:
        if task['id'] == id:
            if request.method == 'POST':
                task['nome'] = request.form['produto']
                task['quantidade'] = int(request.form['quantidade'])
                task['preco'] = float(request.form['preco'])
                return redirect('/lista_produtos')
            return render_template('editar_produto.html', task=task)
    return redirect('/lista_produtos')

@app.route('/excluir-produto/<int:id>')
def excluir_produto(id):
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            break
    return redirect('/lista_produtos')

def calcular_valor_total():
    total = 0
    for task in tasks:
        total += task['quantidade'] * task['preco']
    return total

if __name__ == '__main__':
    app.run(debug=True)
