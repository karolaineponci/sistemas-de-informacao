//Exemplo: manipulando matrizes

#include <iostream>

int main(){

    int mat[3][3] = {{1,2,3},{4,5,6},{7,8,9}};

    std::cout << "Imprimindo a primeira linha\n";

    for(int j = 0; j < 3; j++){
        std::cout <<mat[0][j] << " ";
    }

    std::cout<<"\n";

    std::cout <<"Imprimindo toda a matriz:\n";

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            std::cout << mat[i][j] << " ";
        }
        std::cout << "\n"; //Quebra de linha após cada linha da matriz
    }

    return 0;
}