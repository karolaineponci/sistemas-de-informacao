//Faça um programa que leia os valores de uma matriz 2x2 do usuário e calcule a soma dos elementos da primeira linha.

#include <iostream>

int main(){
    int matriz[2][2];
    int soma = 0;

    std::cout << "Digite os dados da matriz: \n";

    for (int i =0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            std::cout << "Elemento [" << i << "][" << j << "]: ";
            std::cin >> matriz [i][j];
        }
    }

    std::cout <<"\nSoma da matriz: \n";

    for (int j = 0; j < 2; j++) {
        soma += matriz[0][j];
    }
    std::cout << "A soma dos elementos da primeira linha 2: " << soma << "\n";

    return 0;

}