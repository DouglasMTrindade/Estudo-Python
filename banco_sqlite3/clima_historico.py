import sqlite3
from valida_entrada import le_int


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
    conn = sqlite3.connect('consultas.db')
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
        if rows:
            for row in rows:
             print(row)
        else:
            print("Nenhum historico encontrado")
    except sqlite3.Error as e:
        print(f"Erro no banco: {e}")
    finally:
        conn.close()


def filtrar_por_cidade():
    conn = sqlite3.connect('consultas.db')
    cursor = conn.cursor()
    
    cidade = input("Digite a cidade que quer filtrar : ")
    try:
        cursor.execute("SELECT * FROM consultas WHERE cidade = ?" , (cidade,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print(f"ciade '{cidade}' nao encontrada no registro")
    except sqlite3.Error as e:
        print(f"Erro no banco {e}")
    finally:
        conn.close()


def apagar_por_id ():
    conn = sqlite3.connect("consultas.db")
    cursor = conn.cursor()

    print("Historico de consultas:")
    lista_consultas()
    id = le_int("informe o ID a ser excluido: ")

    try:
        sql = "DELETE FROM consultas WHERE id = ?" 
        sql_cont = "SELECT COUNT(*) FROM consultas WHERE id = ?"

        cursor.execute(sql_cont,(id,))
        count = cursor.fetchone()[0]
        print(count)
        if count == 0:
            print(f"ERRO: ID {id} não encontrado")
            return

        cursor.execute(sql, (id,))
        conn.commit()
        print(f"ID {id} apagado com sucesso!")
        print("Historico atualizado:")
        lista_consultas()
    except sqlite3.Error as e:
        print("Erro no banco: ", e)
    finally:
        conn.close()

