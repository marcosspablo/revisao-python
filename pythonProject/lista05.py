primos = []
num = int(input("Digite um número: "))

for c in range(1, num + 1):
    cont = 0

    for y in range(1, c + 1):
        if c % y == 0:
            cont += 1
    if cont == 2:
        primos.append(c)
print(f"Esses são os números primos do intervalo desejado:")
print(primos)