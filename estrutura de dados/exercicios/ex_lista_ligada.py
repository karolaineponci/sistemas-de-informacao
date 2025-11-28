#Construção e Operações Essenciais

# 1.Criar a Classe No (Nó/Link): Crie uma classe No em Java que represente um link da lista. Ela deve ter dois atributos: um para o dado (ex: int dado) e uma referência para o próximo nó (No proximo).

class No:
    def __init__(self, dado): 
        self.dado = dado # armazena o valor (numero, texto, etc.)
        self.proximo = None # Ponteiro para o proximo nó (inica vazio)

# 2.Criar a Classe ListaLigada: Crie a classe principal ListaLigada que contenha uma referência para o primeiro nó da lista (private No primeiro). O construtor deve inicializar primeiro como null.

class ListaLigada:
    def __init__(self):
        self.primeiro = None # lista começa vazia

    # 3. Implementar inserirNoInicio(): Crie um método public void inserirNoInicio(int dado) que crie um novo nó com o dado informado e o adicione no início da lista. Lembre-se de atualizar a referência primeiro

    def inserir_no_inicio(self, dado):
        novo_no = No(dado) #criar novo nó
        novo_no.proximo = self.primeiro # Novo nó aponta para o antigo primeiro - [novo] -> [A] -> [B]
        self.primeiro = novo_no # lista agora começa com o novo nó


    #  4. Implementar mostrarLista(): Crie um método public void mostrarLista() que percorra a lista desde o início e imprima o dado de cada nó no console, no formato  [dado1] -> [dado2] -> null.

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
    
    # 5. Implementar removerDoInicio(): Crie um método public No removerDoInicio() que remova o primeiro nó da lista e o retorne. Se a lista estiver vazia, deve retornar null.

    def remover_do_inicio(self):
        if self.primeiro is None: # Lista vazia?
            return None
        
        removido = self.primeiro #guarda o nó que será removido
        self.primeiro = self.primeiro.proximo # atualiza o primeiro
        return  removido # retorna o nó removido

teste_lista = ListaLigada()
teste_lista.inserir_no_inicio("Teste 1")
teste_lista.inserir_no_inicio("Teste 2")

print("Lista inicial: ")
teste_lista.mostrar_lista()

removido = teste_lista.remover_do_inicio()
print(f"Removido: [{removido.dado}]")

print("Lista após remoção: ")
teste_lista.mostrar_lista()