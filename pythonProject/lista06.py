alturas = []
idades = []
c = 1
for c in range(1, 6):
    if c != 6:
        altura = float(input("Digite sua altura: "))
        idade = int(input("Digite sua idade: "))
        alturas.append(altura)
        idades.append(idade)
    if c == 6:
        break

print(f"A lista inversa das idades:{idades[::-1]}")
print(f"Lista inversa das alturas: {alturas[::-1]}")