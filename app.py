import db
from tkinter import *
from tkinter import ttk
import db

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


def main():
    root.title("Minha Tarefas")
    linhaAtual = 0
    tarefa = Entry(frm,  width=100)
    tarefa.grid(column=0, row=linhaAtual)
    ttk.Button(frm, text="Adicionar", command=lambda: add_tarefa(tarefa.get(), linhaAtual)).grid(
        column=1, row=linhaAtual)
    linhaAtual = linhaAtual+1
    linhaAtual = exibir_tarefas(linhaAtual, ttk, frm)
    root.mainloop()


def exibir_tarefas(linhaAtual, ttk, frm):
    tarefas = db.get_tarefas()
    if len(tarefas.fetchall()) == 0:
        ttk.Label(frm, text="Sem tarefas cadastradas").grid(
            column=0, row=linhaAtual)
        return
    for tarefa in db.get_tarefas():
        id= tarefa[0]
        text = tarefa[1]
        add_tarefa_text(text, id, linhaAtual)
        linhaAtual = linhaAtual + 1

    return linhaAtual


def add_tarefa(text, linhaAtual):
    if (len(text) == 0):
        return
    linhaAtual = linhaAtual+1
    tarefa_id = db.add_tarefa(text)
    add_tarefa_text(text, tarefa_id, linhaAtual)

    return linhaAtual


def add_tarefa_text(texto, id, linhaAtual):
    t = "[{:}] {:<47}".format(id, texto)
    ttk.Label(frm, text=t,width=100).grid(column=0, row=linhaAtual)
    ttk.Button(frm, text="Concluir", command=lambda: concluir_tarefa(id)).grid(
        column=1, row=linhaAtual)


def concluir_tarefa(tarefa_id):
    db.concluir_tarefa(tarefa_id)


if __name__ == "__main__":
    db.criar_base()
    main()
