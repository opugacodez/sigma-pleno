import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
load_dotenv(dotenv_path)

def env(var_name: str, default: str = None) -> str:
    """
    Retorna o valor da variável de ambiente especificada.
    :param var_name: Nome da variável de ambiente.
    :param default: Valor padrão a ser retornado se a variável não for encontrada.
    :return: Valor da variável ou o valor padrão se não for encontrada.
    """
    return os.getenv(var_name, default)
