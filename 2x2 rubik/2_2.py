def cria_movimento(face, sent):
    if face in ("U", "L", "F", "R", "B", "D") and isinstance(sent, bool):
        return "ULFRBD".find(face) + (sent * 6)
    else:
        raise ValueError("cria_movimento: argumentos invalidos")

def obtem_mov_face(mov):
    return "ULFRBD"[mov % 6]

def obtem_mov_sentido(mov):
    return mov > 5

def eh_movimento(mov):
    return mov in range(12)

def movimentos_iguais(mov1, mov2):
    return eh_movimento(mov1) and eh_movimento(mov2) and mov1 == mov2

def movimentos_para_str(mov):
    return ("U'", "L'", "F'", "R'", "B'", "D'", "U", "L", "F", "R", "B", "D")[mov]

def str_para_movimento(Str):
    if Str in ("U'", "L'", "F'", "R'", "B'", "D'"):
        return cria_movimento(Str[0], False)
    elif Str in ("U", "L", "F", "R", "B", "D"):
        return cria_movimento(Str[0], True)
    else:
        raise ValueError("str_para_movimento: argumentos invalidos")

def movimento_inverso(mov):
    return (mov + 6) % 12

def str_para_sequencia(Str):
    return 0

#print(obtem_mov_sentido(cria_movimento("U", True)))
#print(eh_movimento(12))