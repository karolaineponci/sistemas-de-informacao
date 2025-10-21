class No:
    def __init__(self, dado):
        self.dado = dado # O valor armazenado
        self.proximo = None # Ponteiro para o próximo nó

# criando uma lista ligada simples
no1 = No("Maçã")
no2 = No("Melão")
no3 = No("Melancia")
no4 = No("Morango")

# Ligando os nós
no1.proximo = no2 # Maçã > Melão
no2.proximo = no3
no3.proximo = no4

#percorrendo a Lista
atual = no1
while atual:
    print(atual.dado)
    atual = atual.proximo