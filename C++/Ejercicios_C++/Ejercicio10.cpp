// Pida 10 números y cuente cuántos son pares y cuántos impares usando un ciclo for.

#include <iostream>
using namespace std;

int main() {
    int num;
    int pares = 0;
    int impares = 0;

    for (int i = 0; i < 10; ++i) {
        cout << "Ingrese el numero " << (i + 1) << ": ";
        cin >> num;

        if (num % 2 == 0) {
            pares++;
        } else {
            impares++;
        }
    }

    cout << "Cantidad de numeros pares: " << pares << endl;
    cout << "Cantidad de numeros impares: " << impares << endl;

    return 0;
}