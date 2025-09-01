//Faça um algoritmo Preencher um vetor com 300 números reais. Considerando que nenhum dos valores será repetido. Ao final imprimir o menor valor digitado, e o maior valor digitado.

#include <iostream>

int main(){
    float vetor[5]; //para 300 numeroa susbtituir 5 por 300;
    int i;
    float maior;
    float menor;

    std::cout <<"Digite os dados para serem armazenados:\n";

    for (i = 0; i < 5; i++) {
        std::cin >> vetor[i]; 

        if (i == 0){
            maior = vetor[i];
            menor = vetor[i];
        } else {
            if (maior < vetor[i]) {
                maior = vetor[i];
            }
            if (menor > vetor[i]){
                menor = vetor[i];
            }
        }
    }
    std::cout << "\nO maior numeor digitado foi: " << maior << std::endl;
    std::cout << "O menor numero digitado foi: "<< menor << std::endl;

    return 0;

}