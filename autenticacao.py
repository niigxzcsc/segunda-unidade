
import hashlib
import secrets
import hmac


def cadastrar_senha(senha):
    salt = secrets.token_bytes(16)

    hash_senha = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        600000
    )

    return salt.hex(), hash_senha.hex()


def verificar_senha(senha_digitada, salt_hex, hash_original):
    salt = bytes.fromhex(salt_hex)

    novo_hash = hashlib.pbkdf2_hmac(
        "sha256",
        senha_digitada.encode("utf-8"),
        salt,
        600000
    )

    return hmac.compare_digest(
        novo_hash.hex(),
        hash_original
    )


if __name__ == "__main__":
    print("=== CADASTRO DE SENHA ===")

    senha = input("Crie uma senha: ")

    salt, hash_armazenado = cadastrar_senha(senha)

    print("\nCadastro realizado!")

    tentativa = input("Digite sua senha para entrar: ")

    if verificar_senha(tentativa, salt, hash_armazenado):
        print("Acesso autorizado!")
    else:
        print("Senha incorreta!")
