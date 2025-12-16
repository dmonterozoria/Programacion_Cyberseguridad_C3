// Simulador de Firewall Basico - Dennis Montero

#include <iostream>
#include <string>
#include <sstream>
#include <cctype>

using namespace std;

// Funcion para validar IPv4
bool validarIP(const string& ip) {
    int num;
    char punto;
    stringstream ss(ip);

    for (int i = 0; i < 4; i++) {
        if (!(ss >> num)) return false;
        if (num < 0 || num > 255) return false;
        if (i < 3 && !(ss >> punto && punto == '.')) return false;
    }
    return ss.eof();
}

// Convertir string a mayusculas
string aMayusculas(string texto) {
    for (char &c : texto)
        c = toupper(c);
    return texto;
}

// Evaluacion del paquete segun reglas del firewall
bool EvaluarPaquete(string ip, int puerto, string protocolo) {

    bool permiso = false; // Implicit Deny

    // Regla 1: Permitir DNS (UDP 53)
    if (protocolo == "UDP" && puerto == 53)
        permiso = true;

    // Regla 2: Permitir ICMP desde 192.168.x.x
    if (ip.rfind("192.168", 0) == 0 && protocolo == "ICMP")
        permiso = true;

    // Regla 3: Bloqueo explícito RDP (TCP 3389)
    if (protocolo == "TCP" && puerto == 3389)
        permiso = false;

    return permiso;
}

int main() {

    string ip, protocolo;
    int puerto;

    cout << "===== Firewall INFOCORP =====" << endl;

    // Validar IP
    while (true) {
        cout << "Ingrese la IP de origen: ";
        cin >> ip;

        if (validarIP(ip))
            break;
        else
            cout << "Error: IP no valida. Intente de nuevo.\n";
    }

    // Validar puerto
    while (true) {
        cout << "Ingrese el puerto de destino: ";
        cin >> puerto;

        if (cin.fail() || puerto < 0 || puerto > 65535) {
            cout << "Error: puerto invalido.\n";
            cin.clear();
            cin.ignore(1000, '\n');
        } else
            break;
    }

    // Validar protocolo
    while (true) {
        cout << "Ingrese el protocolo (TCP, UDP, ICMP): ";
        cin >> protocolo;

        protocolo = aMayusculas(protocolo);

        if (protocolo == "TCP" || protocolo == "UDP" || protocolo == "ICMP")
            break;
        else
            cout << "Error: protocolo no valido.\n";
    }

    // Evaluacion del paquete
    bool resultado = EvaluarPaquete(ip, puerto, protocolo);

    // Resultado
    cout << "===== Resultado del analisis =====" << endl;
    if (resultado)
        cout << "Paquete permitido\n";
    else
        cout << "Paquete bloqueado\n";

    return 0;
}
