import os
import time

os.system("cls")

print("CRUD: Realizar cadastro de livros onde o usuário poderá cadastrar os seguintes Elementos:"
      "\na) Nome do Livro;"
      "\nb) Nome do Autor;"
      "\nc) Ano de Lançamento;"
      "\nd) Gênero Literário.")
print("\nO programa realizará as seguintes ações:"
      "\na) Criar o cadastro;"
      "\nb) Ler o dado cadastrado;"
      "\nc) Atualizar o cadastro;"
      "\nd) Excluir o cadastro.")

POSICAO_NOME_LIVRO = 0
POSICAO_NOME_AUTOR = 1
POSICAO_ANO_LIVRO = 2
POSICAO_GENERO_LITERARIO = 3
ENCERRAR_PROGRAMA = "Encerrar"

listaMaeDadosDoLivro = []
contadorLivrosCadastrados = 0
contadorPosicaoDoCadastro = 0
posicaoExcluirCadastro = 0
while True:
    decideAcaoDoPrograma = input("\nBem vindo(a) ao LivrosApp, onde você poderá gerenciar o cadastro de seus livros."
                                 "\nPor favor, ajude-nos a decidir algumas ações:"
                                 "\n 1 - Cadastrar um Livro"
                                 "\n 2 - Verificar livro cadastrado"
                                 "\n 3 - Atualizar cadastrado do livro"
                                 "\n 4 - Excluir cadastrado do livro"
                                 "\n 5 - Encerrar sessão"
                                 "\n Escolha: ")
    match decideAcaoDoPrograma:
        case "1":
            nomeDoLivro = input("\nInforme o nome do livro: ").title()
            nomeDoAutor = input("Informe o nome do autor: ").title()
            anoDeLancamento = int(input("Informe o ano de lançamento (Ex: 1992): "))
            generoLiterario = input("Informe o gênero literário: ").title()

            dadosDoLivro = [nomeDoLivro, nomeDoAutor, anoDeLancamento, generoLiterario]
            listaMaeDadosDoLivro.append(dadosDoLivro)
            contadorLivrosCadastrados += 1
            print("\nDados gravados com sucesso!")
            time.sleep(2)
        case "2":
            if contadorLivrosCadastrados == 0:
                print("\nNão há livros cadastrados")
                time.sleep(2)
            else:
                for index in range(len(listaMaeDadosDoLivro)):
                    recebeListaMae = listaMaeDadosDoLivro[index]
                    print(f"\n{contadorPosicaoDoCadastro + 1}º Livro - Nome: {recebeListaMae[POSICAO_NOME_LIVRO]} - "
                          f"Autor: {recebeListaMae[POSICAO_NOME_AUTOR]}"
                          f" - Ano de lançamento: {recebeListaMae[POSICAO_ANO_LIVRO]}"
                          f" - Gênero Literário: {recebeListaMae[POSICAO_GENERO_LITERARIO]}")
                    contadorPosicaoDoCadastro += 1
                print("\nLivros cadastrados em Ordem Numérica")
                contadorPosicaoDoCadastro = 0
                time.sleep(4)
        case "3":
            if contadorLivrosCadastrados == 0:
                print("\nNão há livros cadastrados para alteração!")
                time.sleep(2)
            else:
                atualizaDadosPosicaoLista = int(input("\nInforme a Numeração do Livro cadastrado a ser atualizado: "))
                atualizaDadosPosicaoLista -= 1
                atualizaDadosPosicaoElemento = input("\nInforme qual dado cadastrado você deseja alterar:"
                                                     "\na) - Nome do Livro"
                                                     "\nb) - Nome do Autor"
                                                     "\nc) - Ano do Lançamento"
                                                     "\nd) - Gênero Literário"
                                                     "\nEscolha sua alternativa: ").capitalize()
                match atualizaDadosPosicaoElemento:
                    case "A":
                        nomeDoLivro = input("\nInforme o nome do livro para correção: ").title()
                        listaMaeDadosDoLivro[atualizaDadosPosicaoLista][POSICAO_NOME_LIVRO] = f"{nomeDoLivro}"
                        print("\nAlteração realizada com sucesso!")
                        time.sleep(2)
                    case "B":
                        nomeDoAutor = input("Informe o nome do autor para correção: ").title()
                        listaMaeDadosDoLivro[atualizaDadosPosicaoLista][POSICAO_NOME_AUTOR] = f"{nomeDoAutor}"
                        print("\nAlteração realizada com sucesso!")
                        time.sleep(2)
                    case "C":
                        anoDeLancamento = int(input("Informe o ano de lançamento para correção: (Ex: 1992): "))
                        listaMaeDadosDoLivro[atualizaDadosPosicaoLista][POSICAO_ANO_LIVRO] = f"{anoDeLancamento}"
                        print("\nAlteração realizada com sucesso!")
                        time.sleep(2)
                    case "D":
                        generoLiterario = input("Informe o gênero literário: ").title()
                        listaMaeDadosDoLivro[atualizaDadosPosicaoLista][POSICAO_GENERO_LITERARIO] = f"{generoLiterario}"
                        print("\nAlteração realizada com sucesso!")
                        time.sleep(2)
                    case _:
                        print("\nOps, não identificamos sua alternativa!"
                              "\nAlteração não foi concluída, tente novamente.")
                        time.sleep(2)
        case "4":
            if contadorLivrosCadastrados == 0:
                print("\nNão há livros cadastrados para exclusão!")
                time.sleep(2)
            else:
                posicaoExcluirCadastro = int(input("\nInforme o número do livro cadastrado que deseja excluir: "))
                posicaoExcluirCadastro -= 1
                del listaMaeDadosDoLivro[posicaoExcluirCadastro]
                print("\nCadastro excluído com sucesso!")
                time.sleep(2)
        case "5":
            decideAcaoDoPrograma = ENCERRAR_PROGRAMA
            if decideAcaoDoPrograma == ENCERRAR_PROGRAMA:
                print("\nObrigado por sua preferência!")
                break
        case _:
            print("\nOpção não identificada")
            time.sleep(2)
