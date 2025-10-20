//• Escreva um programa em C que leia uma matriz 3x3 preenchida pelo usuário e exiba apenas os elementos da primeira linha.


#include <iostream>

int main(){
    int mat[3][3];

    std::cout <<"Insira os dados da matriz 4x4. \n";
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            std::cout << "Elemento [" << i << "][" << j << "]: ";
            std::cin >> mat[i][j];
        }
    }

    
    std::cout << "Imprimindo a primeira linha\n";

    for(int j = 0; j < 3; j++){
        std::cout <<mat[0][j] << " ";
    }

    return 0;
}

