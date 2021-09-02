from myFunctions import soma, subtracao, multiplicacao, divisao, potenciacao

print("\nFAÇA OPERAÇÕES MATEMÁTICAS BÁSICAS")

i = 0
continuar = True
minhaLista1 = []
operador = []
minhaLista2 = []
resultado = []


while continuar:

    minhaLista1.append(float(input("\nPrimeiro número: ")))
    operador.append(input("[+] [-] [*] [/] [**]: "))
    minhaLista2.append(float(input("Segundo número: ")))

    if operador[i] == '+':
        resultado.append(soma(minhaLista1, minhaLista2, i))

    elif operador[i] == '-':
        resultado.append(subtracao(minhaLista1, minhaLista2, i))

    elif operador[i] == '*':
        resultado.append(multiplicacao(minhaLista1, minhaLista2, i))

    elif operador[i] == '/':
        while minhaLista2[i] == 0:
            print('Não é possível dividir por 0.')
            minhaLista2[i] = float(input("Segundo número: "))
        resultado.append(divisao(minhaLista1, minhaLista2, i))

    elif operador[i] == '**':
        while minhaLista2[i] == 0 or minhaLista2[i] == 1:
            print('Não é possível elevar a 0 ou 1.')
            minhaLista2[i] = float(input("Segundo número: "))
        resultado.append(potenciacao(minhaLista1, minhaLista2, i))

    continuar = input('Realizar outra operação? [S/N]: ')

    if continuar == 'Sim' or continuar == 'sim' or continuar == 'S' or continuar == 's' or continuar == 'SIM':
        continuar = True
        i += 1

    elif continuar == 'Não' or continuar == 'não' or continuar == 'N' or continuar == 'n' or continuar == 'NÃO'\
            or continuar == 'Nao' or continuar == 'nao' or continuar == 'NAO' or continuar == '':
        print()
        i = 0
        while i < resultado.__len__():
            print(minhaLista1[i], operador[i], minhaLista2[i], '=', resultado[i])
            i += 1
        continuar = False