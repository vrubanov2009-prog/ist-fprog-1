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

#movimento_para_str
def movimento_para_str(mov):
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
        return real_str_para_sequencia(Str[:-2]) + [str_para_movimento(Str[-2:])]
    else:
        return real_str_para_sequencia(Str[:-1]) + [str_para_movimento(Str[-1])]

#sequencia_para_str
def sequencia_para_str(seq):
    return real_sequencia_para_str(list(seq))

def real_sequencia_para_str(seq):
    if seq == []:
        return ""
    else:
        return real_sequencia_para_str(seq[:-1]) + movimento_para_str(seq[-1])

#sequencia_inversa
def sequencia_inversa(seq):
    return tuple(real_sequencia_inversa(list(seq)))

def real_sequencia_inversa(seq):
    if seq == []:
        return []
    else:
        return [movimento_inverso(seq[-1])] + real_sequencia_inversa(seq[:-1])

#simplifica_sequencia
def simplifica_sequencia(seq):
    return tuple(simples(list(seq)))

def simples(seq):
    seq_s = algoritmo_simplificar(seq)
    if seq_s == seq:
        return seq
    else:
        return simples(seq_s)

def peso_mov(mov):
    return (3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1)[mov]

def algoritmo_simplificar(seq, contador = 0):
    if len(seq) == 1:
        if contador == 0:
            return seq
        else:
            return [[], [(seq[-1] % 6) + 6], [(seq[-1] % 6) + 6, (seq[-1] % 6) + 6], [seq[-1] % 6]][(contador + peso_mov(seq[-1])) % 4]
    elif seq[-1] % 6 == seq[-2] % 6:
        return algoritmo_simplificar(seq[:-1], (contador + peso_mov(seq[-1])) % 4)
    else:
        return algoritmo_simplificar(seq[:-1]) + [[], [(seq[-1] % 6) + 6], [(seq[-1] % 6) + 6, (seq[-1] % 6) + 6], [seq[-1] % 6]][(contador + peso_mov(seq[-1])) % 4]




#print(obtem_mov_sentido(cria_movimento("U", True)))
#print(eh_movimento(12))
#print(sequencia_para_str(simplifica_sequencia(str_para_sequencia("U'UUF'FDF"))))
#print(str_para_sequencia("U'UUF'FDF"))
#print(sequencia_inversa((1,5,3,9,10)))