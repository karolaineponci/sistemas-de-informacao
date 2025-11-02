#Construção e Operações Essenciais
    # Manipulação e Variações

class No:
    def __init__(self, dado): 
        self.dado = dado # armazena o valor (numero, texto, etc.)
        self.proximo = None # Ponteiro para o proximo nó (inica vazio)


# 8. Adicionar Referência ao ultimo: Modifique a sua classe ListaLigada para incluir uma referência ao último nó (private No ultimo), transformando-a numa lista com extremidade dupla. Atualize o construtor e os métodos de inserção/remoção para manter esta referência correta. 

class ListaLigada:
    def __init__(self):
        self.primeiro = None # lista começa vazia
        self.ultimo = None # NOVO: referencia ao ultino nó


    def inserir_no_inicio(self, dado):
        novo_no = No(dado) #criar novo nó

        if self.primeiro is None: # lista vazia?
            self.primeiro = novo_no
            self.ultimo = novo_no  # unico elemento =  primeiro e ultimo

        else:
            novo_no.proximo = self.primeiro # Novo nó aponta para o antigo primeiro - [novo] -> [A] -> [B]
            self.primeiro = novo_no # lista agora começa com o novo nó

        print(f"\nInserido no INICIO: [{dado}]")

#9. Implementar inserirNoFim(): Usando a referência ultimo do exercício anterior, crie um método public void inserirNoFim(int dado) que adicione um novo nó no final da lista em tempo O(1).

    def inserir_no_fim(self, dado):
        novo_no = No(dado) #criar novo no

        if self.ultimo is None: # se lista esta vazia
            #primeiro e ultimo são o mesmo nó
            self.primeiro = novo_no
            self.ultimo = novo_no

        else:
            # lista não vazia: conectar ao ultimo
            self.ultimo.proximo = novo_no # ultimo atual aponta para novo
            self.ultimo = novo_no #novo vira o ultimo

        print(f"\nInserido no FIM: [{dado}]")

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

        # MOSTRAR PRIMEIRO E ULTIMO (para debug)
        print(f"\nPrimeiro: {self.primeiro.dado if self.primeiro else 'None'}")
        print(f"\nUltmo: {self.ultimo.dado if self.ultimo else 'None'}")

    def remover_do_inicio(self):
        if self.primeiro is None: # Lista vazia?
            return None
        
        removido = self.primeiro #guarda o nó que será removido

        if self.primeiro == self.ultimo: #só tinha 1 elememto
            self.primeiro = None
            self.ultimo = None
        else:
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
    
    # 7. Implementar remover(int chave): Crie um método public No remover(int chave) que busque por um nó com a chave informada e o remova da lista, religando o nó anterior ao nó posterior. Retorne o nó removido ou null se não for encontrado. (Atenção: este é mais complexo que removerDoInicio()).
    
    def remover(self, chave):
        # Caso 1: lista vazia
        if self.primeiro is None:
            return None
        
        # Caso 2: Remover o primeiro elemento
        if self.primeiro.dado == chave:
            removido = self.primeiro
            self.primeiro = self.primeiro.proximo
            return removido
        
        # Caso 3: remover do meio ou final
        anterior = self.primeiro # ponteiro anterior
        atual = self.primeiro.proximo # ponteiro atual
        # Quando encontra, faz: [anterior] → [próximo] (pula o atual)
         
        while atual:
            if atual.dado == chave:
                # encotrou. religar o anterior ao próximo
                anterior.proximo = atual.proximo
                return atual
            
            # avançar para o próximo nó
            anterior = atual
            atual = atual.proximo

        # caso 4: elemento não encontrado
        return None

# inserindo dados na lista
teste_lista = ListaLigada()
teste_lista.inserir_no_inicio("Teste 1")
teste_lista.inserir_no_fim("Teste 2")
teste_lista.inserir_no_fim("Teste 3")
teste_lista.inserir_no_fim("Teste 4")
teste_lista.inserir_no_inicio(10)
teste_lista.inserir_no_fim(100)

print("\nLista inicial: ") #mostra a lista
teste_lista.mostrar_lista()

removido = teste_lista.remover_do_inicio() #remove
print(f"\nRemovido: [{removido.dado}]")

print("\nLista após remoção: ") #mostra a lista após remoção
teste_lista.mostrar_lista()


resultado1 = teste_lista.buscar("Teste 2") # busca elemento e mostra (se encontrado)
print(f"\nBuscar Teste 1: {resultado1.dado if resultado1 else 'Não encontrado'}")

resultado2 = teste_lista.buscar("Teste 4") # busca elemento e mostra (se encontrar)
print(f"\nBuscar Teste 4: {resultado2.dado if resultado2 else 'Não encontrado'}")

removido = teste_lista.remover("Teste 5")
print(f"\nRemovido: [{removido.dado if removido else 'Não encontrado! Não foi possivel remover.'}]")

print("\nLista após remoção:")
teste_lista.mostrar_lista()