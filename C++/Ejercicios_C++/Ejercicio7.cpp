// Use un ciclo for para imprimir la tabla de multiplicar del número que el usuario ingrese, desde 1 hasta 12.

#include <iostream>
using namespace std;

int main() {
    int numero;

    cout << "Ingrese un numero para ver su tabla de multiplicar: ";
    cin >> numero;

    cout << "Tabla de multiplicar del " << numero << ":\n";
    for (int i = 1; i <= 12; ++i) {
        cout << numero << " x " << i << " = " << numero * i << endl;
    }

    return 0;
}