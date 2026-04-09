from src.database import get_db_connection

def limpar_dados():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Apaga todos os registros da tabela
    cursor.execute("DELETE FROM leituras")
    
    # Reinicia o contador de ID (AUTOINCREMENT) para começar do 1 novamente
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='leituras'")
    
    conn.commit()
    conn.close()
    print("Banco de dados limpo e IDs resetados!")

if __name__ == "__main__":
    limpar_dados()