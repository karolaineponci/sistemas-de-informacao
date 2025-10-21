class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaTarefas:
    def __init__(self):
        self.primeiro = None

    def adicionar_tarefa(self, tarefa):
        nova_tarefa = No(tarefa)
        if not self.primeiro:
            self.primeiro = nova_tarefa
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nova_tarefa
    def mostrar_tarefas(self):
        atual = self.primeiro
        while atual:
            print(f"- {atual.dado}")
            atual = atual.proximo

# usando a lista
minhas_tarefas = ListaTarefas()
minhas_tarefas.adicionar_tarefa("Estudar listas ligadas/encadeadas.")
minhas_tarefas.adicionar_tarefa("Fazer exercicios.")
minhas_tarefas.adicionar_tarefa("Revisar o conteudo.")

print("Minhas Tarefas: ")
minhas_tarefas.mostrar_tarefas()