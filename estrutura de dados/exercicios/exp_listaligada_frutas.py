class No: # defnindo a classe No (molde para criar cada elemento da lista)
    
    def __init__(self, dado): # método construtor - executado quando criamos um novo objeto da classe
        self.dado = dado # Atributo dado: guarda o valor que este nó armazena - ex>: Maça, morango...

        self.proximo = None #Atributo proximo: Ponteiro que aponta para o próximo nó (inicialmente não aponta para ninguem - None)

# criando uma lista ligada simples
# CRIANDO OBJETOS (instâncias da classe No)
# Cada linha abaixo cria um objeto independente:
no1 = No("Maçã")
no2 = No("Melão")
no3 = No("Melancia")
no4 = No("Morango")

# LIGANDO OS OBJETOS PARA FORMAR UMA LISTA ENCADEADA
# Criando as conexões entre os nós:
no1.proximo = no2 # Maçã > Melão
no2.proximo = no3
no3.proximo = no4

#percorrendo a Lista
atual = no1
while atual:
    print(atual.dado)
    atual = atual.proximo