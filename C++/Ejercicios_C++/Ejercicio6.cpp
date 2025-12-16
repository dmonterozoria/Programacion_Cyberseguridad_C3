// Cree un struct Producto con nombre, precio y cantidad. Registre 5 productos y calcule el valor total del inventario.

#include <iostream>
using namespace std;

struct Producto {
    string nombre;
    float precio;
    int cantidad;
};

int main() {
    Producto productos[5];
    float valorTotalInventario = 0;

    cout << "--- Registro de Productos ---" << endl;
    for (int i = 0; i < 5; ++i) {
        cout << "Ingrese el nombre del producto " << (i + 1) << ": ";
        cin >> productos[i].nombre;
        cout << "Ingrese el precio del producto " << (i + 1) << ": ";
        cin >> productos[i].precio;
        cout << "Ingrese la cantidad del producto " << (i + 1) << ": ";
        cin >> productos[i].cantidad;
    }

    // Calcular el valor total del inventario
    for (int i = 0; i < 5; ++i) {
        valorTotalInventario += productos[i].precio * productos[i].cantidad;
    }

    cout << "\nEl valor total del inventario es: $" << valorTotalInventario << endl;

    return 0;
}