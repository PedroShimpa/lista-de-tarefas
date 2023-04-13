import sqlite3
from datetime import datetime


db_name = 'database'

conn = sqlite3.connect(db_name+".db")


def criar_base():
    conn.cursor()
    conn.execute("""
    create table if not exists tarefas (
        id integer primary key autoincrement,
        tarefa text,
        concluido integer,
        created text,
        concluida_em text
    )
    """)


def add_tarefa(tarefa):

    created = datetime.now()
    conn.execute(
        "insert into tarefas (tarefa, concluido,created) values (?,?,?)", (tarefa, 0, created, ))
    conn.commit()


def remover_tarefa(id):
    conn.execute("delete from tarefas where id = ?", (id))
    conn.commit()


def concluir_tarefa(id):
    concluida_em = datetime.now()
    conn.execute(
        "update tarefas set concluido = ?, concluida_em = ?", (1, concluida_em, ))
    conn.commit()


def get_tarefas():
    return conn.execute("select id, tarefa, concluido from tarefas where concluido != 1")


def get_tarefas_concluidas():
    return conn.execute("select id, tarefa from tarefas where concluido != 0")
