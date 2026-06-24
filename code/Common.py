import inspect
from pathlib import Path

def gameLog(log_type=0, message: str = "sem mensagem"):
    archive = getArchive()

    if log_type == 0:
        log_type = "LOG"
    elif log_type == 1:
        log_type = "WARNING"
    elif log_type == 2:
        log_type = "ERROR"
    else:
        log_type = "UNDEFINED"

    print(f"[{archive}][{log_type}]: {message}")

    saida = {
        "archive": archive,
        "type": log_type,
        "message": message
    }

    return saida


def getArchive():
    # Pega o frame do chamador (nível 1 da pilha)
    frame_chamador = inspect.stack()[1]

    # Extrai o caminho completo e depois apenas o nome do arquivo
    caminho_arquivo = frame_chamador.filename
    nome_arquivo = Path(caminho_arquivo).name

    return nome_arquivo