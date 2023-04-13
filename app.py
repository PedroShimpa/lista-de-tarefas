import db
from tkinter import *
import tkinter as tk
from tkinter import ttk
import db

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


def main():
    root.title("Minhas Tarefas")
    linhaAtual = 0
    ttk.Button(frm, text="Ver Concluidas", command=exibir_concluidas).grid(
        column=0, row=linhaAtual)
    linhaAtual = linhaAtual + 1
    terefaInput = Entry(frm,  width=100)
    terefaInput.grid(column=0, row=linhaAtual)
    ttk.Button(frm, text="Adicionar", command=lambda: add_tarefa(terefaInput.get())).grid(
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
        id = tarefa[0]
        text = tarefa[1]
        add_tarefa_text(text, id, linhaAtual, frm)
        linhaAtual = linhaAtual + 1

    return linhaAtual


def add_tarefa(text):
    if (len(text) == 0):
        return
    db.add_tarefa(text)
    main()


def add_tarefa_text(texto, id, linhaAtual, frm):
    t = "[{:}] {:<47}".format(id, texto)
    ttk.Label(frm, text=t, width=100).grid(column=0, row=linhaAtual)
    ttk.Button(frm, text="Concluir", command=lambda: concluir_tarefa(id, linhaAtual)).grid(
        column=1, row=linhaAtual)


def concluir_tarefa(tarefa_id, linhaAtual):
    db.concluir_tarefa(tarefa_id)


def exibir_concluidas():
    modal = tk.Toplevel(root)
    table = ttk.Treeview(modal)
    table["columns"] = ("tarefa")
    table.heading("tarefa", text="Tarefa")
    row = 0
    for tarefa in db.get_tarefas_concluidas():
        row = row+1
        table.insert("", "end", text=row, values=[tarefa[1]])
    scroll_x = ttk.Scrollbar(modal, orient=tk.HORIZONTAL, command=table.xview)
    scroll_y = ttk.Scrollbar(modal, orient=tk.VERTICAL, command=table.yview)
    table.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    table.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    db.criar_base()
    main()
