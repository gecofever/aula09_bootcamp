def decorator(func):
    def interna(*args):
        resultado = func(*args)
        return resultado

    return interna



@decorator
def repete(repeticao):
    contador = 0
    while contador < repeticao:
        print("REPETINDO")
        contador += 1

#funcionando = decorator(repete(3))