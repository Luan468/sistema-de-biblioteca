# Sistema de Gerenciamento de Livros

## Descrição

Este projeto consiste em um sistema de gerenciamento de livros feito em Python.

O sistema permite cadastrar, listar, buscar, emprestar e devolver livros, além de
possibilitar a ordenação dos livros cadastrados.

O objetivo do projeto é praticar conceitos básicos da linguagem Python, como
funções, listas, dicionários, estruturas de repetição e arquivos.

## Funcionalidades

- Cadastrar novos livros.
- Listar os livros cadastrados.
- Buscar livros pelo título ou autor.
- Registrar empréstimos.
- Registrar devoluções.
- Ordenar os livros por título, autor ou ano.
- Salvar os dados dos livros em um arquivo.
- Carregar os livros salvos ao iniciar o programa.

## Como funciona

Ao iniciar o programa, será apresentado um menu com as opções disponíveis.

O usuário pode escolher uma das opções:

1. Cadastrar livro
2. Emprestar livro
3. Devolver livro
4. Listar livros
5. Buscar livro
6. Ordenar livros
7. Sair

Os livros são armazenados no arquivo `livros.txt`, permitindo que os dados
continuem salvos mesmo depois que o programa for encerrado.

## Estrutura dos livros

Cada livro possui as seguintes informações:

- Título
- Autor
- Ano de publicação
- Código/ISBN
- Status

O status do livro pode ser:

- Disponível
- Emprestado

## Tecnologias utilizadas

- Python
- Visual Studio Code
- Arquivo de texto (`livros.txt`)

## Como executar

1. Instale o Python no computador.
2. Abra a pasta do projeto no Visual Studio Code.
3. Abra o terminal.
4. Execute o seguinte comando:

```bash
python biblioteca.py