
from criptografia import criptografar, descriptografar
from hash_senha import gerar_hash, comparar_hash
from autenticacao import cadastrar_senha, verificar_senha
from forca_bruta import simular_forca_bruta


def menu():
    print("\n================================")
    print("   SISTEMA DE PROTEÇÃO DE DADOS")
    print("================================")
    print("1 - Criptografar mensagem")
    print("2 - Descriptografar mensagem")
    print("3 - Gerar hash SHA-256")
    print("4 - Comparar hash")
    print("5 - Cadastrar e verificar senha")
    print("6 - Simular força bruta")
    print("0 - Sair")
    print("================================")


def executar():
    while True:
        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mensagem = input("Digite a mensagem: ")
            deslocamento = int(input("Deslocamento: "))

            resultado = criptografar(mensagem, deslocamento)

            print("Mensagem criptografada:", resultado)

        elif opcao == "2":
            mensagem = input("Digite a mensagem: ")
            deslocamento = int(input("Deslocamento: "))

            resultado = descriptografar(mensagem, deslocamento)

            print("Mensagem original:", resultado)

        elif opcao == "3":
            texto = input("Digite o texto: ")

            print("Hash SHA-256:", gerar_hash(texto))

        elif opcao == "4":
            texto = input("Digite o texto: ")
            hash_original = input("Digite o hash original: ")

            if comparar_hash(texto, hash_original):
                print("Os hashes são iguais!")
            else:
                print("Os hashes são diferentes!")

        elif opcao == "5":
            senha = input("Cadastre uma senha: ")

            salt, hash_senha = cadastrar_senha(senha)

            tentativa = input("Confirme sua senha: ")

            if verificar_senha(tentativa, salt, hash_senha):
                print("Autenticação realizada com sucesso!")
            else:
                print("Senha incorreta!")

        elif opcao == "6":
            senha = input("Digite uma senha fictícia para teste: ")

            simular_forca_bruta(senha)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    executar()

from criptografia import criptografar, descriptografar
from hash_senha import gerar_hash, comparar_hash
from autenticacao import cadastrar_senha, verificar_senha
from forca_bruta import simular_forca_bruta


def menu():
    print("\n================================")
    print("   SISTEMA DE PROTEÇÃO DE DADOS")
    print("================================")
    print("1 - Criptografar mensagem")
    print("2 - Descriptografar mensagem")
    print("3 - Gerar hash SHA-256")
    print("4 - Comparar hash")
    print("5 - Cadastrar e verificar senha")
    print("6 - Simular força bruta")
    print("0 - Sair")
    print("================================")


def executar():
    while True:
        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mensagem = input("Digite a mensagem: ")
            deslocamento = int(input("Deslocamento: "))

            resultado = criptografar(mensagem, deslocamento)

            print("Mensagem criptografada:", resultado)

        elif opcao == "2":
            mensagem = input("Digite a mensagem: ")
            deslocamento = int(input("Deslocamento: "))

            resultado = descriptografar(mensagem, deslocamento)

            print("Mensagem original:", resultado)

        elif opcao == "3":
            texto = input("Digite o texto: ")

            print("Hash SHA-256:", gerar_hash(texto))

        elif opcao == "4":
            texto = input("Digite o texto: ")
            hash_original = input("Digite o hash original: ")

            if comparar_hash(texto, hash_original):
                print("Os hashes são iguais!")
            else:
                print("Os hashes são diferentes!")

        elif opcao == "5":
            senha = input("Cadastre uma senha: ")

            salt, hash_senha = cadastrar_senha(senha)

            tentativa = input("Confirme sua senha: ")

            if verificar_senha(tentativa, salt, hash_senha):
                print("Autenticação realizada com sucesso!")
            else:
                print("Senha incorreta!")

        elif opcao == "6":
            senha = input("Digite uma senha fictícia para teste: ")

            simular_forca_bruta(senha)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    executar()
