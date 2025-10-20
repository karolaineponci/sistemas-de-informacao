//Exemplo: leitura matrizes

#include <iostream>

int main(){
    int matriz[2][2];

    std::cout << "Digite os valores da matriz 2x2: \n";

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            std::cout << "Elemento [" << i << "][" << j << "]: ";
            std::cin >> matriz[i][j];
        }
    }

    std::cout << "\nMatriz 2x2x:\n";
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            std::cout << matriz[i][j] << " ";
        }
        std::cout << "\n";
    }



    return 0;
}