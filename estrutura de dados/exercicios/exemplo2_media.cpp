#include <iostream>

int main(){
    int v[5] = {10, 20, 30, 40, 50}; //tamanho do vetor e valores
    int i;
    float s = 0; // será usado para somar os valores do vetor dentro do for 

    for (i = 0; i < 5; i++){
        s+= v[i];
    }

    std::cout << "Resultado: "<< s / 5 << std::endl;

    return 0;
}