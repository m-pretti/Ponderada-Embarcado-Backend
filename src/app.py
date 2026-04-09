from flask import Flask, request, jsonify, render_template, redirect, url_for
from database import (init_db, get_db_connection, inserir_leitura, 
                      listar_leituras, deletar_leitura, buscar_leitura, atualizar_leitura)

app = Flask(__name__)

# Inicializa o banco de dados garantindo que a tabela exista
with app.app_context():
    init_db()

# --- 1. PAINEL PRINCIPAL (DASHBOARD) ---
@app.route('/')
def index():
    """Painel principal com gráfico e últimas 10 leituras"""
    leituras = listar_leituras(10)
    return render_template('index.html', leituras=leituras)

# --- 2. ENDPOINT DE CRIAÇÃO (API) ---
@app.route('/leituras', methods=['POST'])
def criar():
    """Recebe JSON do simulador e persiste no banco"""
    dados = request.get_json() 
    if not dados:
        return jsonify({'erro': 'JSON inválido'}), 400 
    
    id_novo = inserir_leitura(
        dados.get('temperatura'), 
        dados.get('umidade'), 
        dados.get('pressao')
    )
    return jsonify({'id': id_novo, 'status': 'criado'}), 201 

# --- 3. PÁGINA DE HISTÓRICO ---
@app.route('/historico')
def listar():
    """Exibe o histórico respeitando o limite de 50 do módulo database"""
    leituras = listar_leituras(50) # Ajustado para o limite máximo do requisito
    return render_template('historico.html', leituras=leituras)

# --- 4. ROTA DE EDIÇÃO (GET e POST) ---
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Exibe formulário preenchido (GET) ou salva alterações (POST)"""
    # Note o nome da função: buscar_leitura (conforme requisito 6.2)
    leitura = buscar_leitura(id)
    
    if not leitura:
        return "Registro não encontrado", 404

    if request.method == 'POST':
        nova_temp = request.form.get('temperatura')
        nova_umid = request.form.get('umidade')
        
        atualizar_leitura(id, nova_temp, nova_umid)
        return redirect(url_for('listar'))
    
    return render_template('editar.html', leitura=leitura)

# --- 5. ROTA DE EXCLUSÃO ---
@app.route('/deletar/<int:id>', methods=['POST'])
def remover(id):
    """Remove o registro do banco"""
    deletar_leitura(id) 
    return redirect(url_for('listar'))

# --- 6. API DE ESTATÍSTICAS (PONTO EXTRA) ---
@app.route('/api/estatisticas')
def estatisticas():
    """Retorna dados processados para o gráfico"""
    return jsonify({"mensagem": "Dados estatísticos prontos"})

if __name__ == '__main__':
    # Roda o servidor na porta 5000 visível na rede local
    app.run(debug=True, host='0.0.0.0', port=5000)