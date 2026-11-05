# Jogo de Adivinhação de Palavras (Wordle)

palavra_secreta = "mosias"
tentativas = 0

# Criando a dica inicial com sublinhados
dica_inicial = ""
for letra in palavra_secreta:
    dica_inicial += "_ "

print("Bem-vindo ao jogo de adivinhação de palavras!")
print(f"Sua dica é: {dica_inicial.strip()}")

acertou = False

while not acertou:
    palpite = input("Qual é o seu palpite? ").lower()
    tentativas += 1

    # Verifica se acertou de primeira
    if palpite == palavra_secreta:
        acertou = True
        print("Parabéns! Você adivinhou!")
        print(f"Você precisou de {tentativas} palpites.")

    # Se errou, verifica se o tamanho é diferente
    elif len(palpite) != len(palavra_secreta):
        print(
            "Desculpe, o palpite precisa ter o mesmo número de letras que a palavra secreta.\n"
        )

    # Se o tamanho for igual, gera a dica com as regras de maiúsculas e minúsculas
    else:
        dica = ""
        for i in range(len(palavra_secreta)):
            letra_palpite = palpite[i]
            letra_secreta = palavra_secreta[i]

            if letra_palpite == letra_secreta:
                # Posição correta: maiúscula
                dica += letra_palpite.upper() + " "
            elif letra_palpite in palavra_secreta:
                # Presente na palavra, mas posição errada: minúscula
                dica += letra_palpite.lower() + " "
            else:
                # Não existe na palavra: sublinhado
                dica += "_ "

        print(f"Sua dica é: {dica.strip()}")