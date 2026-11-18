
def criptografar(mensagem, deslocamento):
    resultado = ""

    for caractere in mensagem:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')

            nova_letra = chr(
                (ord(caractere) - base + deslocamento) % 26 + base
            )

            resultado += nova_letra
        else:
            resultado += caractere

    return resultado


def descriptografar(mensagem, deslocamento):
    return criptografar(mensagem, -deslocamento)
