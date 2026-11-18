
def simular_forca_bruta(senha_alvo):
    possibilidades = [
        "1234",
        "admin",
        "senha",
        "123456",
        "python",
        "abc123",
        "senha123",
        "seguranca2026"
    ]

    tentativas = 0
    encontrada = False

    print("\n=== SIMULAÇÃO DE FORÇA BRUTA ===")

    for tentativa in possibilidades:
        tentativas += 1

        print(f"Tentativa {tentativas}: {tentativa}")

        if tentativa == senha_alvo:
            encontrada = True
            print("\nSenha descoberta!")
            print(f"Senha: {tentativa}")
            break

    if not encontrada:
        print("\nSenha não encontrada na lista de testes.")

    print(f"Total de tentativas: {tentativas}")

    return encontrada


if __name__ == "__main__":
    senha = input("Digite uma senha de teste: ")

    simular_forca_bruta(senha)
