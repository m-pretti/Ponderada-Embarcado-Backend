import sqlite3

def get_db_connection():
    """Retorna uma conexão configurada com row_factory para acesso por nome de coluna"""
    conn = sqlite3.connect('dados.db', timeout=10)
    conn.execute('PRAGMA journal_mode=WAL')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Cria as tabelas se não existirem (executa o schema.sql)"""
    conn = get_db_connection()
    try:
        # Tenta localizar o schema.sql independente de onde o script é chamado
        try:
            with open('src/schema.sql', 'r') as f:
                conn.executescript(f.read())
        except FileNotFoundError:
            with open('schema.sql', 'r') as f:
                conn.executescript(f.read())
        print("Banco de dados inicializado com sucesso!")
    finally:
        conn.close()

def inserir_leitura(temperatura, umidade, pressao=None):
    """Realiza o INSERT dos dados meteorológicos"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO leituras (temperatura, umidade, pressao) VALUES (?, ?, ?)",
        (temperatura, umidade, pressao)
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return novo_id

def listar_leituras(limite=50):
    """Retorna um SELECT com as últimas leituras (Limite padrão: 50)"""
    conn = get_db_connection()
    # Garante que o limite não ultrapasse 50 conforme requisito do módulo
    leituras = conn.execute(
        'SELECT * FROM leituras ORDER BY timestamp DESC LIMIT ?', 
        (min(limite, 50),)
    ).fetchall()
    conn.close()
    return leituras

def buscar_leitura(id):
    """Realiza o SELECT por ID para edição ou consulta específica"""
    conn = get_db_connection()
    leitura = conn.execute('SELECT * FROM leituras WHERE id = ?', (id,)).fetchone()
    conn.close()
    return leitura

def atualizar_leitura(id, temperatura, umidade):
    """Realiza o UPDATE dos dados de uma leitura específica"""
    conn = get_db_connection()
    conn.execute(
        "UPDATE leituras SET temperatura = ?, umidade = ? WHERE id = ?",
        (temperatura, umidade, id)
    )
    conn.commit()
    conn.close()

def deletar_leitura(id):
    """Realiza o DELETE de um registro por ID"""
    conn = get_db_connection()
    conn.execute('DELETE FROM leituras WHERE id = ?', (id,))
    conn.commit()
    conn.close()