# Definindo a palavra a ser adivinhada
import random
from erros import erros

palavras = ['amor', 'carinho', 'paixao', 'produtos']
palavra = random.choice(palavras)

# Inicializa o progresso do jogador com sublinhados para cada letra da palavra
progresso = ['_' for _ in palavra]

# Variável para contar o número de erros
erros_cometidos = 0
max_erros = len(erros) - 1  # Número máximo de erros antes do jogo terminar

print('Seja bem-vindo ao jogo da forca!')
print(f"A palavra tem {len(palavra)} letras: {' '.join(progresso)}")

opcao = input('Continuar = Enter, Sair = S: ').lower()

while True:
    if opcao == 's':
        print('Jogo encerrado, obrigado!')
        break

    # Mostra o boneco da forca correspondente ao número de erros
    print(erros[erros_cometidos])

    # Mostra o progresso atual da palavra
    print(' '.join(progresso))

    letra = input('Informe uma letra: ').lower()

    # Verifica se a letra está na palavra
    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                progresso[i] = letra  # Substitui o sublinhado pela letra correta
    else:
        erros_cometidos += 1  # Incrementa o número de erros
        print(f"A letra '{letra}' não está na palavra.")
    
    # Verifica se o jogador perdeu (erros atingiram o máximo permitido)
    if erros_cometidos == max_erros:
        print(erros[erros_cometidos])  # Mostra o último estágio do boneco
        print(f"Você perdeu! A palavra era: {palavra}")
        break

    # Verifica se o jogador adivinhou a palavra completa
    if '_' not in progresso:
        print(f"Parabéns! Você adivinhou a palavra: {palavra}")
        break