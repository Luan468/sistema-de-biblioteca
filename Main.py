ARQUIVO = "livros.txt"


# Carrega os livros salvos no arquivo
def carregar_livros():
    livros = []

    try:
        arquivo = open(ARQUIVO, "r", encoding="utf-8")

        for linha in arquivo:
            dados = linha.strip().split(";")

            if len(dados) == 5:
                livro = {
                    "titulo": dados[0],
                    "autor": dados[1],
                    "ano": dados[2],
                    "codigo": dados[3],
                    "status": dados[4]
                }

                livros.append(livro)