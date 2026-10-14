#cria_movimento
def cria_movimento(face, sent):
    if face in ("U", "L", "F", "R", "B", "D") and isinstance(sent, bool):
        return "ULFRBD".find(face) + (sent * 6)
    else:
        raise ValueError("cria_movimento: argumentos invalidos")

#obtem_mov_face
def obtem_mov_face(mov):
    return "ULFRBD"[mov % 6]

#obtem_mov_sentido
def obtem_mov_sentido(mov):
    return mov > 5

#eh_movimento
def eh_movimento(mov):
    return mov in range(12)

#movimentos_iguais
def movimentos_iguais(mov1, mov2):
    return eh_movimento(mov1) and eh_movimento(mov2) and mov1 == mov2

#movimentos_para_str
def movimentos_para_str(mov):
    return ("U'", "L'", "F'", "R'", "B'", "D'", "U", "L", "F", "R", "B", "D")[mov]

#str_para_movimento
def str_para_movimento(Str):
    if Str in ("U'", "L'", "F'", "R'", "B'", "D'"):
        return cria_movimento(Str[0], False)
    elif Str in ("U", "L", "F", "R", "B", "D"):
        return cria_movimento(Str[0], True)
    else:
        raise ValueError("str_para_movimento: argumentos invalidos")

#movimento_inverso
def movimento_inverso(mov):
    return (mov + 6) % 12

#str_para_sequencia
def str_para_sequencia(Str):
    return tuple(real_str_para_sequencia(Str))

def real_str_para_sequencia(Str):
    if Str == "":
        return []
    elif Str[-1] == "'":
        return str_para_sequencia(Str[:-2]) + [str_para_movimento(Str[-2:])]
    else:
        return str_para_sequencia(Str[:-1]) + [str_para_movimento(Str[-1])]

#sequencia_para_str
def sequencia_para_str(seq):
    return real_sequencia_para_str(list(seq))

def real_sequencia_para_str(seq):
    if seq == []:
        return ""
    else:
        return real_sequencia_para_str(seq[:-1]) + [movimentos_para_str(seq[-1])]

#sequencia_inversa
def sequencia_inversa(seq):
    return tuple(real_sequencia_inversa(list(seq)))

def real_sequencia_inversa(seq):
    if seq == []:
        return []
    else:
        return [seq[-1]] + real_sequencia_inversa[seq[:-1]]

#simplifica_sequencia
def simplifica_sequencia(seq):
    return tradusir_de_simples(simplificar(tradusir_para_simples(list(str_para_sequencia(seq)))))

def tradusir_para_simples(seq):
    return [curto(seq), contagem(seq)]

def contagem(seq):
    if len(seq) == 1:
        return 1
    elif seq[-1] % 6 == seq[-2] % 6:
        return ((seq[-1] // 6) * 3) + contagem(seq[:-1])
    else:
        return ((seq[-1] // 6) * 3) + (contagem(seq[:-1]) * 10)

def curto(seq):
    if len(seq) == 1:
        return seq
    elif seq[-1] == seq[-2]:
        return curto(seq[:-1])
    else:
        return curto(seq[:-1]) + [seq[-1]]




#print(obtem_mov_sentido(cria_movimento("U", True)))
#print(eh_movimento(12))
print(tradusir_para_simples(list(str_para_sequencia("U'UUF'FDF"))))