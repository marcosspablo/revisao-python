nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >=7 and media <10:
    print("Você foi aprovado!")
elif media <7:
    print("Você foi reprovado!")
elif media ==10:
    print("Aprovado com Distinção")