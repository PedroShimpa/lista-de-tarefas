import sqlite3

conn = sqlite3.connect("assembleia.db")

def criar_base():
    conn.cursor()
    conn.execute("""
    create table if not exists tarefas (
        cd_tarefa integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
    """)


def add_tarefa(tarefa):
    cursor = conn.cursor()
    cursor.execute(
        "insert into tarefas (tarefa, concluido) values (?, 0)", (tarefa, ))
    return cursor.lastrowid


def remover_tarefa(cd_tarefa):
    conn.execute("delete from tarefas where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()


def concluir_tarefa(cd_tarefa):
    conn.execute(
        "update tarefas set concluido = 1 where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()


def get_tarefas():
    return conn.execute("select cd_tarefa, tarefa, concluido from tarefas where concluido != 1")

def get_tarefas_concluidas():
    return conn.execute("select cd_tarefa, tarefa, concluido from tarefas where concluido != 0")
