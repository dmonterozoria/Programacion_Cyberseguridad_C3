// Escriba un programa que calcule el área de un rectángulo pidiendo base y altura (float).

#include <iostream>
using namespace std;

int main() {
    float base, altura, area;

    cout << "--- Calculo del area de un rectangulo ---" << endl;
    cout << "Ingrese la base del rectangulo: ";
    cin >> base;
    cout << "Ingrese la altura del rectangulo: ";
    cin >> altura;

    area = base * altura;

    cout << "El area del rectangulo es: " << area << endl;

    return 0;
}