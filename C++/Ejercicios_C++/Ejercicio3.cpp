// Convierta grados Celsius a Fahrenheit usando un valor ingresado por el usuario.

#include <iostream>
using namespace std;

int main() {
    float celsius, fahrenheit;

    cout << "--- Conversion de Celsius a Fahrenheit ---" << endl;
    cout << "Ingrese la temperatura en grados Celsius: ";
    cin >> celsius;

    fahrenheit = (celsius * 9 / 5) + 32;

    cout << "La temperatura en grados Fahrenheit es: " << fahrenheit << endl;

    return 0;
}