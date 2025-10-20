//


#include <iostream>

int main(){
    int matriz[2][2];
    int soma = 0;

    std::cout << "Digite os dados da matriz: \n";

    for (int i =0; i < 2; i++){
        for (int j = 0; j < 2; j++){
            std::cout << "Elemento [" << i << "][" << j << "]: ";
            std::cin >> matriz [i][j];
            soma += matriz[i][j];
        }
    }

    std::cout<<"A soma de toda a matriz e: "<< soma;

    return 0;
}