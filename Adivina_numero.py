numero_objetivo = int(input("Di un numero del 1 al 20: "))
while numero_objetivo <= 0 or numero_objetivo > 20:
    print("Eres idiota? No seas cuñao")
    numero_objetivo = int(input("Di un numero del 1 al 20: "))
numero_user = 0

print("adivina el numero que estoy pensando (del 1 al 20):")
while numero_objetivo != numero_user:
    numero_user = int(input())
    if numero_user <= 0 or numero_user > 20:
        print("Eres idiota? Te dije del 1 al 20\nDespedido")
        break
    
    print("otra vez: ")

if numero_objetivo == numero_user:
    print("EPIC WIN")


