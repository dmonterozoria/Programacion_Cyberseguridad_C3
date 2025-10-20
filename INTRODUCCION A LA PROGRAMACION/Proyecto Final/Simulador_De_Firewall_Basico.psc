Función permiso <- EvaluarPaquete(ip,puerto,protocolo)
	Definir permiso Como Lógico
	// Todo esta bloqueado por defecto (Implicit Deny)
	permiso <- Falso
	// Reglas del Firewall
	// Regla 1: Permitir DNS
	Si protocolo='UDP' Y puerto=53 Entonces
		permiso <- Verdadero
	FinSi
	// Regla 2: Permitir el ping (ICMP) desde la red local "192.168.x.x"
	Si Subcadena(ip,1,7)='192.168' Y protocolo='ICMP' Entonces
		permiso <- Verdadero
	FinSi
	// Regla 3: Bloqueo explicito de RDP
	Si protocolo='TCP' Y puerto=3389 Entonces
		permiso <- Falso
	FinSi
FinFunción

Algoritmo SimuladorDeFirewallBasico
	Definir ip Como Cadena
	Definir puerto Como Entero
	Definir protocolo Como Cadena
	Definir resultado Como Lógico
	Escribir '===== Firewall INFOCORP ====='
	Escribir 'Ingrese la IP de origen:'
	Leer ip
	Escribir 'Ingrese el puerto de destino:'
	Leer puerto
	Escribir 'Ingrese el protocolo (TCP, UDP, ICMP):'
	Leer protocolo
	resultado <- EvaluarPaquete(ip,puerto,protocolo)
	Si resultado Entonces
		Escribir 'Paquete permitido'
	SiNo
		Escribir 'Paquete Bloqueado'
	FinSi
FinAlgoritmo