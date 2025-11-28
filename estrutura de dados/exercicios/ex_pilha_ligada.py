# Parte 2: Implementação de Pilha e Fila com Lista Ligada (8 Exercícios) Conforme visto na apresentação, Pilhas e Filas são Tipos Abstratos de Dados. Agora, vamos implementá-los usando listas ligadas como estrutura interna, em vez de arrays.

    # Implementação de Pilha (LIFO)
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.primeiro = None
    
    def inserir_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no

    def remover_inicio(self):
        if self.primeiro is None:
            return None
        removido = self.primeiro
        return removido
    
    def ver_primeiro(self):
        if self.primeiro is None:
            return None
        return self.primeiro.dado
    def esta_vazia(self):
        return self.primeiro is None
    
# 13.Criar a Classe PilhaLigada: Crie uma classe PilhaLigada. Internamente, ela deve usar uma ListaLigada (pode ser a que você já criou) para armazenar os dados.

class PilhaLigada:
    def __init__(self):
        self.lista = ListaLigada()  #lista interna

    # 14.Implementar push(int dado): Crie o método push para a sua PilhaLigada. Esta operação deve usar o método inserirNoInicio() da sua lista ligada interna, pois a inserção e remoção no topo da pilha são feitas no início da lista (operação O(1)).

    def push(self, dado):
        self.lista.inserir_inicio(dado)
        print(f"Push: {dado}")

    # 15.Implementar pop(): Crie o método pop que remove e retorna o elemento do topo da pilha. Ele deve usar o método removerDoInicio() da sua lista ligada.

    def pop(self):
        if self.lista.esta_vazia():
            print("Pilha vazia - não fazer pop")
            return None
        
        removido = self.lista.remover_inicio()
        print(f"Pop: {removido.dado}")
        return removido.dado
    
    # 16.Implementar peek() e isEmpty(): Crie o método peek que apenas "espia" o valor no topo sem removê-lo, e o método isEmpty que verifica se a pilha está vazia.

    def peek(self):
        if self.lista.esta_vazia():
            print("👀 Peek: Pilha vazia")
            return None
        
        topo = self.lista.ver_primeiro()
        print(f"👀 Peek: {topo}")
        return topo
    
    def is_empty(self):
        vazia = self.lista.esta_vazia()
        print(f"📭 isEmpty: {vazia}")
        return vazia
    
    def mostrar_pilha(self):
        if self.lista.esta_vazia():
            print("Pilha: [VAZIA]")
            return
        
        print("Pilha (topo → base): ", end="")
        atual = self.lista.primeiro
        while atual:
            print(f"[{atual.dado}]", end="")
            if atual.proximo:
                print(" ↓ ", end="")
            else:
                print(" (base)", end="")
            atual = atual.proximo
        print()


# TESTANDO A PILHA
print("=== PILHA COM LISTA LIGADA ===")

pilha = PilhaLigada()

print("\n1. Pilha vazia:")
pilha.mostrar_pilha()  # Pilha: [VAZIA]
pilha.is_empty()       # isEmpty: True

print("\n2. Push de elementos:")
pilha.push(10)  
pilha.push(20)   
pilha.push(30)  

pilha.mostrar_pilha()  

print("\n3. Peek no topo:")
pilha.peek()

print("\n4. Pop de elementos:")
pilha.pop()   
pilha.pop()   

pilha.mostrar_pilha()  

print("\n5. Últimas operações:")
pilha.peek()    
pilha.is_empty()  # isEmpty: False

pilha.pop()   
pilha.is_empty()  # isEmpty: True
pilha.mostrar_pilha()  # Pilha: [VAZIA]
