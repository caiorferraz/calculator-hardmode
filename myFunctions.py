
def soma(lista1, lista2, indice):
    return lista1[indice] + lista2[indice]

def subtracao(lista1, lista2, indice):
    return lista1[indice] - lista2[indice]

def multiplicacao(lista1, lista2, indice):
    return lista1[indice] * lista2[indice]

def divisao(lista1, lista2, indice):
    return lista1[indice] / lista2[indice]

def potenciacao(lista1, lista2, indice):
    return lista1[indice] ** lista2[indice]

def apuraVotacao(listaCandidatos, listaVotos, totalVotos, qtdCandidatos):
    for i in range(qtdCandidatos):
        print(listaCandidatos[i], ':', listaVotos[i], '(', (listaVotos[i] / totalVotos) * 100, '%)')