class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir_inicio(self, dado):
        novo_no = No(dado)
        if self.ultimo is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no
    def remover_inicio(self):
        if self.primeiro is None:
            return None
        
        removido = self.primeiro
        if self.primeiro == self.ultimo: # so tinha 1 elemento
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo

        return removido
    
    def ver_primeiro(self):
        if self.primeiro is None:
            return None
        return self.primeiro.dado

    def esta_vazia(self):
        return self.primeiro is None

class FilaLigada:
    def __init__(self):
        self.lista = ListaLigada() # Lista interna com primeiro e último

    def enqueue(self, dado):
        self.lista.inserir_inicio(dado)
        print(f"Enqueue: {dado}")

    # 19.Implementar dequeue() (Desenfileirar): Crie o método dequeue que remove e retorna o elemento do início da fila. Ele deve usar o método removerDoInicio() da sua lista.

    def dequeue(self):
        if self.lista.esta_vazia():
            print("Fila vazia - não pode fazer daqueue")
            return None
        
        removido = self.lista.remover_inicio()
        print(f"Dequeue: {removido.dado}")
        return removido.dado
    
    #  20.Implementar peek() e isEmpty(): Crie os métodos peek (para ver o primeiro da fila) e isEmpty para a sua FilaLigada.

    def peek(self):
        if self.lista.esta_vazia():
            print(" Peek: Fila vazia")
            return None
        
        frente = self.lista.ver_primeiro()
        print(f" Peek: {frente}")
        return frente
    
    def is_empty(self):
        vazia = self.lista.esta_vazia()
        print(f" isEmpty: {vazia}")
        return vazia
    
    def mostrar_fila(self):
        if self.lista.esta_vazia():
            print("Fila: [VAZIA]")
            return
        
        print("Fila (frente → fim): ", end="")
        atual = self.lista.primeiro
        while atual:
            print(f"[{atual.dado}]", end="")
            if atual.proximo:
                print(" → ", end="")
            else:
                print(" (fim)", end="")
            atual = atual.proximo
        print()



# TESTANDO A FILA

fila = FilaLigada()

print("\n1. Fila vazia:")
fila.mostrar_fila()  # Fila: [VAZIA]
fila.is_empty()      # isEmpty: True

print("\n2. Enqueue de elementos:")
fila.enqueue("Cliente A")  #  Enqueue: Cliente A
fila.enqueue("Cliente B")  #  Enqueue: Cliente B  
fila.enqueue("Cliente C")  #  Enqueue: Cliente C

fila.mostrar_fila()  # Fila (frente → fim): [Cliente A] → [Cliente B] → [Cliente C] (fim)

print("\n3. Peek na frente:")
fila.peek()  #  Peek: Cliente A

print("\n4. Dequeue de elementos:")
fila.dequeue()   #  Dequeue: Cliente A
fila.dequeue()   #  Dequeue: Cliente B

fila.mostrar_fila()  # Fila (frente → fim): [Cliente C] (fim)

print("\n5. Últimas operações:")
fila.peek()      #  Peek: Cliente C
fila.is_empty()  # isEmpty: False

fila.dequeue()   #  Dequeue: Cliente C
fila.is_empty()  # isEmpty: True
fila.mostrar_fila()  # Fila: [VAZIA]