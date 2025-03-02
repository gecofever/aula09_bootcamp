import time

def decorator(funcao):
    def wrapper():
        print('Estou antes da execução da função')
        funcao()
        print('Estou depois da execução da função')

    return wrapper

def outra_funcao():
    print('Sou um argumento')

funcao_decorada = decorator(outra_funcao)
funcao_decorada()


def calcula_duracao(executa):
    def wraper():
        tempo_inicial = time.time()
        executa()
        tempo_final = time.time()

        tempo_total = tempo_final - tempo_inicial

        print(f'Tempo total de execuçãoda função [main]: {tempo_total}')

    return wraper

@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

main()