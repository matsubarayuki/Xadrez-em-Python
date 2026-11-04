def criar_tabuleiro():
    """Cria um tabuleiro 8x8 com as peças nas posições iniciais."""

    tabuleiro = [
        ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
        ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
        ["□", "■", "□", "■", "□", "■", "□", "■"],
        ["■", "□", "■", "□", "■", "□", "■", "□"],
        ["□", "■", "□", "■", "□", "■", "□", "■"],
        ["■", "□", "■", "□", "■", "□", "■", "□"],
        ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
        ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    ]

    return tabuleiro


def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro."""

    print("\n    a   b   c   d   e   f   g   h")

    for i in range(8):
        print(f"{8 - i}   ", end="")

        for j in range(8):
            print(tabuleiro[i][j], end="   ")

        print("")
    
    print()


def posicao_valida(linha, coluna):
    """Verifica se a posição está dentro dos limites."""

    return 0 <= linha < 8 and 0 <= coluna < 8


def mover_peca(tabuleiro, origem, destino):
    """Move uma peça de uma posição para outra."""

    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    if not posicao_valida(linha_origem, coluna_origem):
        print("Posição de origem inválida!")
        return False

    if not posicao_valida(linha_destino, coluna_destino):
        print("Posição de destino inválida!")
        return False

    if tabuleiro[linha_origem][coluna_origem] in ["□", "■"]:
        print("Não existe peça na posição de origem!")
        return False

    # Guarda a peça e a cor da casa de origem
    peca = tabuleiro[linha_origem][coluna_origem]
    casa_origem = "□" if (linha_origem + coluna_origem) % 2 == 0 else "■"

    # Move a peça
    tabuleiro[linha_destino][coluna_destino] = peca
    tabuleiro[linha_origem][coluna_origem] = casa_origem

    print("Peça movida com sucesso!")
    return True


# Programa principal
if __name__ == "__main__":

    tabuleiro = criar_tabuleiro()

    mostrar_tabuleiro(tabuleiro)