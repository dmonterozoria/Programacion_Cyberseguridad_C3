// Pida al usuario su nombre (string), edad (int) y estatura (float). Luego imprima toda la información en formato de ficha.

#include <iostream>
using namespace std;

int main() {
    string nombre;
    int edad;
    float estatura;

    cout << "--- Ficha Personal ---" << endl;
    cout << "Ingrese su nombre: ";
    getline(cin, nombre);
    cout << "Ingrese su edad: ";
    cin >> edad;
    cout << "Ingrese su estatura (en metros): ";
    cin >> estatura;

    cout << "\n--- Ficha ---" << endl;
    cout << "Nombre: " << nombre << endl;
    cout << "Edad: " << edad << " años" << endl;
    cout << "Estatura: " << estatura << " metros" << endl;

    return 0;
}