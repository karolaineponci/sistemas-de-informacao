//Um algoritmo que apresente 5 números inteiros e realize a media aritmética entre eles

#include <iostream>

int main(){

int v[5];  //tamanho do vetor
float media;  //variavel para armazenar a media

v[0] = 50;
v[1] = 40;
v[2] = 30;
v[3] = 20;
v[4] = 10;

media = (v[0] + v[1] + v[2] + v[3] + v[4]) / 5.0;

std::cout << "A media aritimetida dos numeros e: " << media << std::endl;

return 0;

}