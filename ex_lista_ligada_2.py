#Construção e Operações Essenciais
    # Manipulação e Variações

class No:
    def __init__(self, dado): 
        self.dado = dado # armazena o valor (numero, texto, etc.)
        self.proximo = None # Ponteiro para o proximo nó (inica vazio)


class ListaLigada:
    def __init__(self):
        self.primeiro = None # lista começa vazia


    def inserir_no_inicio(self, dado):
        novo_no = No(dado) #criar novo nó
        novo_no.proximo = self.primeiro # Novo nó aponta para o antigo primeiro - [novo] -> [A] -> [B]
        self.primeiro = novo_no # lista agora começa com o novo nó


    def mostrar_lista(self):
        atual = self.primeiro #começa pelo primeiro nó
        while atual: # enquanto não chegar no final
            print(f"[{atual.dado}]", end="")
            if atual.proximo:
                print(" -> ", end="") # Tem próximo? Mostra seta
            else:
                print(" -> null", end="") # chegou no final
            atual = atual.proximo #vai para o proximo nó
        print() # Pula linha no final
    

    def remover_do_inicio(self):
        if self.primeiro is None: # Lista vazia?
            return None
        
        removido = self.primeiro #guarda o nó que será removido
        self.primeiro = self.primeiro.proximo # atualiza o primeiro
        return  removido # retorna o nó removido
    
    #  6. Implementar buscar(int chave): Crie um método public No buscar(int chave) que percorra a lista e retorne o nó que contém o valor da chave. Se não encontrar, deve retornar null.

    def buscar(self, chave):
        atual = self.primeiro # começa pelo primeiro nó

        while atual: # percorre toda a lista
            if atual.dado == chave:
                return atual #retorna o no encontrado
            atual = atual.proximo
        return None
    

teste_lista = ListaLigada()
teste_lista.inserir_no_inicio("Teste 1")
teste_lista.inserir_no_inicio("Teste 2")

print("Lista inicial: ")
teste_lista.mostrar_lista()

removido = teste_lista.remover_do_inicio()
print(f"Removido: [{removido.dado}]")

print("Lista após remoção: ")
teste_lista.mostrar_lista()