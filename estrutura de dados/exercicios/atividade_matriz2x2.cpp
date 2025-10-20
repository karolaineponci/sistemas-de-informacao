//• Faça um programa em que preencha uma matriz 2x2 com o número 7 em todas as posições e, em seguida, exiba a matriz.

#include <iostream>

int main() {
    int mat[2][2];

    std::cout << "Digite 7 todoscos valores da matriz 2x2: \n";

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            std::cout << "Elemento [" << i << "]["<< j << "]: ";
            std::cin >> mat[i][j];
        }
    }



    return 0;
}