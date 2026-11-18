
import hashlib


def gerar_hash(texto):
    return hashlib.sha256(
        texto.encode("utf-8")
    ).hexdigest()


def comparar_hash(texto, hash_original):
    hash_novo = gerar_hash(texto)

    return hash_novo == hash_original


if __name__ == "__main__":
    senha = input("Digite um texto para gerar o hash: ")

    resultado = gerar_hash(senha)

    print("\nHash SHA-256:")
    print(resultado)
