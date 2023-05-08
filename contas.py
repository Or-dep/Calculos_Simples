def multiplicacao(valor, mutiplicador):#1
    resultado = valor*mutiplicador
    return resultado


def divisao(valor, divisor):#2
    resultado = valor/divisor
    return resultado


def divisaoInt(valor, divisor):#3
    resultado = valor//divisor
    return resultado


def somar(valor, soma):#4
    resultado = valor+soma
    return resultado


def subtracao(valor, subtrair):#5
    resultado = valor-subtrair
    return resultado


def exponenciacao(valor, potencia):#6
    resultado = valor**potencia
    return resultado


def restoDivisao(valor, resto):#7
    resultado = valor%resto
    return resultado


def escolha(x):
    value = int(input("Qual 1°valor?"))
    value2 = int(input("Qual 2°valor?"))

    if x == 1:
        result = multiplicacao(value, value2)

    elif x == 2:
        result = divisao(value, value2)

    elif x == 3:
        result = divisaoInt(value,value2)

    elif x == 4:
        result = somar(value, value2)

    elif x == 5:
        result = subtracao(value, value2)

    elif x == 6:
        result = exponenciacao(value,value2)

    elif x == 7:
        result = restoDivisao(value,value2)

    return f"\nResultado da conta: {result}\n"


print("\nEscolha qual tipo de conta\n\n1 - Multiplicação\n2 - Divisão\n3 - Divisão Exata\n4 - Soma\n5 - Subtração\n6 - Exponenciação\n7 - Resto da Divisão\n")

valores = int(input("Qual sua Escolha: "))

print(escolha(valores))