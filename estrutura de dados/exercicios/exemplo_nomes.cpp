//Faça um algoritmo que preencha um vetor com 25 nomes e depois imprima os nomes digitados

#include <iostream>

int main(){
    char nomes[5][50];  //para fazer com 25 nomes subistitui o tamanho do vetor de 5 para 25;
    
    int i;

    std::cout <<"Digite os nomes: \n";

    //for para ler os nomes
    for (i = 0; i < 5; i++) {
        std::cout << "Nome " << i + 1 << ": ";
        std::cin >> nomes [i]; //cin é para ler e armazenar o nome na variavel nomes
    }

    std::cout << "\nNomes digitados: \n";

    for (i = 0; i < 5; i++) {
        std::cout << nomes [i] << "\n";
    }

    return 0;

}