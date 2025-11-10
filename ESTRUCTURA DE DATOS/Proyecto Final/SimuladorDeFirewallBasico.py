import ipaddress

def EvaluarPaquete(ip: str, puerto: int, protocolo: str) -> bool:

    permiso = False  #Todo esta bloqueado por defecto (Implicit Deny)

    #Regla 1: Permitir DNS (UDP puerto 53)
    if protocolo.upper() == 'UDP' and puerto == 53:
        permiso = True

    #Regla 2: Permitir ping (ICMP) desde la red local "192.168.x.x"
    if ip.startswith("192.168") and protocolo.upper() == 'ICMP':
        permiso = True

    #Regla 3: Bloqueo explicito de RDP (TCP 3389)
    if protocolo.upper() == 'TCP' and puerto == 3389:
        permiso = False

    return permiso


def main():
    print("===== Firewall INFOCORP =====")

    #Validar IP
    while True:
        ip = input("Ingrese la IP de origen: ").strip()
        try:
            ipaddress.ip_address(ip)
            break  # Si es válida, salir del bucle
        except ValueError:
            print(f"❌ Error: '{ip}' no es una IP válida. Intente de nuevo.")

    #Validar puerto
    while True:
        try:
            puerto = int(input("Ingrese el puerto de destino: ").strip())
            if 0 <= puerto <= 65535:
                break
            else:
                print("❌ Error: el puerto debe estar entre 0 y 65535.")
        except ValueError:
            print("❌ Error: el puerto debe ser un número entero.")

    #Validar protocolo
    protocolos_validos = {"TCP", "UDP", "ICMP"}
    while True:
        protocolo = input("Ingrese el protocolo (TCP, UDP, ICMP): ").strip().upper()
        if protocolo in protocolos_validos:
            break
        else:
            print("❌ Error: protocolo no válido. Debe ser TCP, UDP o ICMP.")

    #Evaluacion del paquete
    resultado = EvaluarPaquete(ip, puerto, protocolo)

    #Resultado
    if resultado:
        print("✅ Paquete permitido")
    else:
        print("⛔ Paquete bloqueado")


#Ejecutar el programa principal
if __name__ == "__main__":
    main()