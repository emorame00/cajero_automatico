# Constantes: reglas del cajero.
SALDO_INICIAL = 250000
RETIRO_MINIMO = 5000
RETIRO_MAXIMO = 100000

# Variables: saldo, contador y acumulador.
saldo = SALDO_INICIAL
retiros_exitosos = 0
total_retirado = 0

print("Bienvenido al cajero automático")
print("Saldo inicial: ₡", saldo)
continuar = input("¿Desea realizar un retiro? (s/n): ").strip().lower()

# Repetir mientras el usuario quiera y el saldo alcance para retirar.
while continuar == "s" and saldo >= RETIRO_MINIMO:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto < RETIRO_MINIMO or monto > RETIRO_MAXIMO:
        print("Retiro rechazado: monto fuera de límites.")
        print("Retiro mínimo: ₡", RETIRO_MINIMO)
        print("Retiro máximo: ₡", RETIRO_MAXIMO)
    elif monto > saldo:
        print("Retiro rechazado: fondos insuficientes.")
    else:
        saldo = saldo - monto
        retiros_exitosos = retiros_exitosos + 1
        total_retirado = total_retirado + monto
        print("Retiro realizado.")

    print("Saldo actualizado: ₡", saldo)

    if saldo >= RETIRO_MINIMO:
        continuar = input("¿Desea continuar retirando? (s/n): ")
        continuar = continuar.strip().lower()
    else:
        print("El saldo no alcanza para otro retiro.")

# Resumen: se muestra después de salir del ciclo.
print("\nResumen de operaciones")
print("Saldo restante: ₡", saldo)
print("Cantidad de retiros exitosos:", retiros_exitosos)
print("Total de dinero retirado: ₡", total_retirado)
