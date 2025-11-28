# 10.Implementar ListaDuplamenteLigada: Crie uma nova estrutura de dados ListaDuplamenteLigada. Para isso, a classe No deverá ter uma referência para o nó anterior e para o proximo. Implemente os métodos inserirNoInicio() e mostrarDoInicio().

class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None #aponta para nó anterior
        self.proximo = None #aponta para proximo

class ListaDuplamenteLigada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir_no_inicio(self, dado):
        novo_no = NoDuplo(dado)

        if self.primeiro is None: #lista vazia
            self.primeiro = novo_no
            self.ultimo = novo_no

        else:
            #conectar o novo nó com o primeiro atual
            novo_no.proximo = self.primeiro
            self.primeiro.anterior = novo_no  #primeiro atual aponta para novo
            self.primeiro = novo_no

        print(f"\nInserindo do Inicio: [{dado}]")

    def mostrar_do_inicio(self):
        atual = self.primeiro

        print("\nDo inicio ao fim: ", end="")

        while atual:
            print(f"[{atual.dado}]", end="")

            if atual.proximo:
                print(" ⇄ ", end="") #seta dupla para mosstrar bidirecional
            
            else:
                print(" -> null", end="")
            atual = atual.proximo
        print()

    #  11.Implementar mostrarDoFim(): Na sua ListaDuplamenteLigada, crie um método public void mostrarDoFim() que use a referência anterior para percorrer e imprimir a lista de trás para a frente.

    def mostrar_do_fim(self):
        atual = self.ultimo #começa pelo ultimo

        print("Do Fim ao Inicio: ", end="")

        while atual:
            print(f"[{atual.dado}]", end="")
            if atual.anterior:
                print(" ⇄ ", end="")
            else:
                print(" -> null", end="")
            atual = atual.anterior
        print()

    #  12.Desafio - Inverter a Lista: Crie um método na ListaLigada simples (public void inverter()) que inverta a ordem dos nós da lista sem criar uma nova lista. (Dica: você precisará de três referências: anterior, atual e proximo).

    def inverter(self):
        anterior = None
        atual = self.primeiro

        while atual: 
            proximo = atual.proximo # guarda o proximo
            atual.proximo = anterior # inverter a seta
            anterior = atual # avançar anterior
            atual = proximo   # avança atual

        self.primeiro = anterior # ultimo vira primeiro

#criar lista duplamente ligada
lista_dupla = ListaDuplamenteLigada()

lista_dupla.inserir_no_inicio(10)
lista_dupla.inserir_no_inicio("livro")
lista_dupla.inserir_no_inicio("filme")
lista_dupla.inserir_no_inicio(50)

print("\nLista original")
lista_dupla.mostrar_do_inicio()
lista_dupla.mostrar_do_fim()


lista_dupla.inverter()
print("\nLista invertida:")
lista_dupla.mostrar_do_inicio()