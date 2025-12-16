// Cree un struct llamado Estudiante con nombre, edad y promedio. Registre 3 estudiantes e imprima el mejor promedio.

#include <iostream>
using namespace std;

struct Estudiante {
    string nombre;
    int edad;
    float promedio;
};

int main() {
    Estudiante estudiantes[3];

    cout << "--- Registro de Estudiantes ---" << endl;
    for (int i = 0; i < 3; ++i) {
        cout << "Ingrese el nombre del estudiante " << (i + 1) << ": ";
        cin >> estudiantes[i].nombre;
        cout << "Ingrese la edad del estudiante " << (i + 1) << ": ";
        cin >> estudiantes[i].edad;
        cout << "Ingrese el promedio del estudiante " << (i + 1) << ": ";
        cin >> estudiantes[i].promedio;
    }

    // Encontrar el estudiante con el mejor promedio
    Estudiante* mejorEstudiante = &estudiantes[0];
    for (int i = 1; i < 3; ++i) {
        if (estudiantes[i].promedio > mejorEstudiante->promedio) {
            mejorEstudiante = &estudiantes[i];
        }
    }

    cout << "\n--- Mejor promedio ---" << endl;
    cout << "Nombre: " << mejorEstudiante->nombre << endl;
    cout << "Edad: " << mejorEstudiante->edad << endl;
    cout << "Promedio: " << mejorEstudiante->promedio << endl;

    return 0;
}