from loguru import logger
from sys import stderr

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO"
)

# Exemplo de uso do logger
logger.info("Este é um log de informação.")
logger.error("Este é um log de erro.")





logger.add("app_teste.log")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Voce digitou corretamente {soma}")
        return soma
    except:
        logger.critical("Digite os numeros corretos.")

print(soma(1,3))
print(soma(1,"3"))