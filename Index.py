def soma(n1, n2):
    return n1 + n2


soma_1 = soma(130, 5)
soma_2 = soma(300, 56)


def resultado(soma1, soma2):
    if soma1 > soma2:
        return "A primeira soma e maior que a segunda soma"
    else:
        return " A segunda soma é maior que a primeira soma"



resultado_1 = resultado(soma_1, soma_2)
print(resultado_1)


def grade(prova1, prova2):
    resultado = (prova1 + prova2) / 2

    if resultado > 6:
        return "Você foi aprovado!"
    else:
        return " Você foi reprovado!"



Alberto = grade(1, 3) 
print(Alberto)

Paulo = grade(7, 9)
print(Paulo)