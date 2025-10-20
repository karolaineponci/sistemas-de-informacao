//Escreva um programa que declare uma matriz 4x4 de inteiros e preencha os valores manualmente no código. Em seguida, exiba a matriz no formato de tabela usando dois loops for.

#include <iostream>

int main(){
    int matriz[4][4] = {{0,1,3,4}, {4,5,6,7}, {0,1,2,3}, {4,5,6,7}};

    std::cout << "Exibindo a matriz 4x4: \n";

    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            std::cout <<matriz[i][j]<<" ";
        }
        std::cout << "\n";
    }


    return 0;
}