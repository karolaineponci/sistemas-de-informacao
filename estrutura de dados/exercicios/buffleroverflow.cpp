#include <iostream>

// Em C++ não existe verificação automática de limites de vetor.

int main() {
    int v[5];
    int i;
    for (i = 0; i < 6; i++) { //Isso causa estouro de memória (buffer overflow), porque v[5] não existe.
    std::cout << "Insira um dado: ";
    std::cin >> v[i];
    }
    std::cout << "\nDados inseridos:\n";
    for (i = 0; i < 6; i++) {
    std::cout << v[i] << "\n";
    }
    return 0;
}