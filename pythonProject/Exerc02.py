while True:
    nota = float(input("Digite uma Nota: "))
    if nota > 10 or nota <0:
        print("Digite um número válido")
    else:
        break
print(f'Sua nota é {nota}')
