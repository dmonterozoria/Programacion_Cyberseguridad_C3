// Use un ciclo while para pedir números hasta que el usuario ingrese 0. Al final muestre la suma total.

#include <iostream>
using namespace std;

int main() {
    int numero;
    int suma = 0;

    cout << "Ingrese numeros para sumar (ingrese 0 para terminar): " << endl;

    while (true) {
        cin >> numero;
        if (numero == 0) {
            break;
        }
        suma += numero;
    }

    cout << "La suma total es: " << suma << endl;

    return 0;
}