// Escriba un programa con un menú (sumar, restar, multiplicar, salir) usando do–while.

#include <iostream>
using namespace std;

int main() {
    int opcion;
    float num1, num2, resultado;

    do {
        cout << "\n--- MENU ---\n";
        cout << "1. Sumar\n";
        cout << "2. Restar\n";
        cout << "3. Multiplicar\n";
        cout << "4. Salir\n";
        cout << "Seleccione una opcion (1-4): ";
        cin >> opcion;

        if (opcion >= 1 && opcion <= 3) {
            cout << "Ingrese el primer numero: ";
            cin >> num1;
            cout << "Ingrese el segundo numero: ";
            cin >> num2;
        }

        switch (opcion) {
            case 1:
                resultado = num1 + num2;
                cout << "El resultado de la suma es: " << resultado << endl;
                break;
            case 2:
                resultado = num1 - num2;
                cout << "El resultado de la resta es: " << resultado << endl;
                break;
            case 3:
                resultado = num1 * num2;
                cout << "El resultado de la multiplicacion es: " << resultado << endl;
                break;
            case 4:
                cout << "Saliendo del programa..." << endl;
                break;
            default:
                cout << "Opcion invalida. Por favor intente de nuevo." << endl;
        }

    } while (opcion != 4);

    return 0;
}