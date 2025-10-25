import sqlite3



def cria_tabela():
    conn = sqlite3.connect('consultas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS consultas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cidade TEXT,
                   temperatura TEXT,
                   descricao TEXT,
                   data_hora TEXT
                   )''')
    conn.commit()
    conn.close()


def salva_consulta (local,clima,agora):
    conn=sqlite3.connect('consultas.db')
    cursor = conn.cursor()

    sql = "INSERT INTO consultas(cidade, temperatura, descricao, data_hora) VALUES (?,?,?,?)"
    dados =(
        local['cidade'],
        clima['temperatura'],
        clima['descricao'],
        agora
    )

    try:

        cursor.execute (sql, dados)
        conn.commit()
    
    except sqlite3.Error as e:
        print(f"Erro no banco: {e}")

    finally:
        conn.close()


def lista_consultas():
    conn =sqlite3.connect('consultas.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM consultas")
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro no banco: {e}")

    for row in rows:
        print(row)

    conn.close()


def filtrar_por_cidade(cidade):
    conn = sqlite3.connect('consultas.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM consultas")
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro no banco {e}")

    for row in rows:
        if row[1] == cidade:
            print(row)
    
    conn.close()


def apagar_por_id (id):



'''
def menu():
'''