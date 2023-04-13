import sqlite3
db_name = 'database'

conn = sqlite3.connect(db_name+".db")


def criar_base():
    conn.cursor()
    conn.execute("""
    create table if not exists tarefas (
        id integer primary key autoincrement,
        tarefa text,
        prioridade text,
        concluido integer
    )
    """)

def add_tarefa(tarefa):
    conn.execute(
        "insert into tarefas (tarefa, concluido) values (?, 0)", (tarefa, ))
    conn.commit()

   

def remover_tarefa(id):
    conn.execute("delete from tarefas where id = ?", (id))
    conn.commit()

def concluir_tarefa(id):
    conn.execute("update tarefas set concluido = ?", (1, ))
    conn.commit()


def get_tarefas():
    return conn.execute("select id, tarefa, concluido from tarefas where concluido != 1")


def get_tarefas_concluidas():
    return conn.execute("select id, tarefa from tarefas where concluido != 0")
