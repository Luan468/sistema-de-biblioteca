ARQUIVO = "livros.txt"


# Carregar os livros
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

        arquivo.close()

    except FileNotFoundError:
        pass

    return livros
# Salvar os livros
def salvar_livros(livros):
    arquivo = open(ARQUIVO, "w", encoding="utf-8")

    for livro in livros:
        linha = (
            livro["titulo"] + ";" +
            livro["autor"] + ";" +
            livro["ano"] + ";" +
            livro["codigo"] + ";" +
            livro["status"] + "\n"
        )

        arquivo.write(linha)

    arquivo.close()


# Cadastrar livro
def cadastrar(livros):
    print("\nCadastro de Livro")

    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    codigo = input("Código/ISBN: ")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "codigo": codigo,
        "status": "Disponível"
    }

    livros.append(livro)

    salvar_livros(livros)

    print("Livro cadastrado com sucesso!")


# Emprestar livro
def emprestar(livros):
    codigo = input("Digite o código do livro: ")

    encontrado = False

    for livro in livros:
        if livro["codigo"] == codigo:
            encontrado = True

            if livro["status"] == "Disponível":
                livro["status"] = "Emprestado"

                salvar_livros(livros)

                print("Livro emprestado com sucesso!")
            else:
                print("Esse livro já está emprestado.")

            break

    if not encontrado:
        print("Livro não encontrado.")
# Devolver livro
def devolver(livros):
    codigo = input("Digite o código do livro: ")

    encontrado = False

    for livro in livros:
        if livro["codigo"] == codigo:
            encontrado = True

            if livro["status"] == "Emprestado":
                livro["status"] = "Disponível"

                salvar_livros(livros)

                print("Livro devolvido com sucesso!")
            else:
                print("Esse livro já está disponível.")

            break

    if not encontrado:
        print("Livro não encontrado.")


# Listar livros
def listar(livros):
    if not livros:
        print("\nNenhum livro cadastrado.")
        return

    print("\nLista de Livros")

    for livro in livros:
        print("-------------------------")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Código:", livro["codigo"])
        print("Status:", livro["status"])


# Buscar livro
def buscar(livros):
    busca = input("Digite o título ou autor: ").lower()

    encontrou = False

    for livro in livros:
        titulo = livro["titulo"].lower()
        autor = livro["autor"].lower()

        if busca in titulo or busca in autor:
            print("-------------------------")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("Código:", livro["codigo"])
            print("Status:", livro["status"])

            encontrou = True

    if not encontrou:
        print("Livro não encontrado.")
        