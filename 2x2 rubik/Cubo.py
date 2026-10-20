def cria_cor(n_cor):
    if n_cor in ("1", "2", "3", "4", "5", "6"):
        return int(n_cor)
    else:
        raise ValueError("cria_cor: argumentos invalidos")

def eh_cor(cor_i):
    return cor_i in range(1, 7)

def cores_iguais(v, u):
    return eh_cor(v) and eh_cor(u) and v == u

def cor_para_str(cor_i):
    return str(cor_i)

def cor_para_int(cor_i):
    return cor_i










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











def cria_cubo():
    return [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

#cria_cubo_de_str
def cria_cubo_de_str(Str):
    if len(Str) == 24:
        for i in range(24):
            if not eh_cor(Str[i]):
                raise ValueError("cria_cubo_de_str: argumentos invalidos")
    return [Str[i] for i in (0, 4, 8, 12, 16, 20, 1, 5, 9, 13, 17, 21, 2, 6, 10, 14, 18, 22, 3, 7, 11, 15, 19, 23)]

#cria_copia_cubo
def cria_copia_cubo(cubo):
    return cubo.copy()

#obtem_cor_face
def obtem_cor_face(cubo, face):
    if face in ("U", "L", "F", "R", "B", "D"):
        a = "ULFRBD".find(face)
    else:
        raise ValueError("obtem_cor_face: argumentos invalidos")
    return tuple([cubo[a + i * 6] for i in range(4)])

#roda_cubo
#o primeiro de transformacoes, o U', foi feito por mim, o resto feito com IA, o U' estava correto :)
transformacoes = (
    (6, 10, 7, 8, 9, 5, 18, 1, 2, 3, 4, 11, 0, 13, 14, 15, 16, 17, 12, 19, 20, 21, 22, 23),
    (0, 13, 2, 3, 4, 17, 6, 19, 8, 9, 10, 11, 12, 7, 14, 15, 16, 5, 18, 1, 20, 21, 22, 23),
    (0, 1, 8, 3, 4, 5, 6, 7, 20, 9, 10, 11, 12, 13, 2, 15, 16, 17, 18, 19, 14, 21, 22, 23),
    (0, 1, 2, 15, 4, 5, 6, 7, 8, 21, 10, 11, 12, 13, 14, 3, 16, 17, 18, 19, 20, 9, 22, 23),
    (4, 1, 2, 3, 22, 5, 6, 7, 8, 9, 16, 11, 12, 13, 14, 15, 10, 17, 18, 19, 20, 21, 0, 23),
    (0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 23, 12, 13, 14, 15, 16, 5, 18, 19, 20, 21, 22, 17),
    (12, 7, 8, 9, 10, 5, 0, 2, 3, 4, 1, 11, 18, 13, 14, 15, 16, 17, 6, 19, 20, 21, 22, 23),
    (0, 19, 2, 3, 4, 17, 6, 13, 8, 9, 10, 11, 12, 1, 14, 15, 16, 5, 18, 7, 20, 21, 22, 23),
    (0, 1, 14, 3, 4, 5, 6, 7, 2, 9, 10, 11, 12, 13, 20, 15, 16, 17, 18, 19, 8, 21, 22, 23),
    (0, 1, 2, 9, 4, 5, 6, 7, 8, 21, 10, 11, 12, 13, 14, 3, 16, 17, 18, 19, 20, 15, 22, 23),
    (22, 1, 2, 3, 0, 5, 6, 7, 8, 9, 4, 11, 12, 13, 14, 15, 10, 17, 18, 19, 20, 21, 16, 23),
    (0, 1, 2, 3, 4, 17, 6, 7, 8, 9, 10, 5, 12, 13, 14, 15, 16, 23, 18, 19, 20, 21, 22, 11)
)

def roda_cubo(cubo, mov):
    return [cubo[i] for i in transformacoes[mov]]

#eh_cubo
def eh_cubo(cubo):
    if len(cubo) != 24:
        return False
    else:
        for i in range(24):
            if not eh_cor(cubo[i]):
                return False
        return True

#eh_cubo_valido
def eh_cubo_valido(cubo):
    a = [0, 0, 0, 0, 0, 0]
    for i in range(24):
        a[cubo[i] - 1] = a[cubo[i] - 1] + 1
    return tuple(a) == (4, 4, 4, 4, 4, 4)

#cubos_iguais
def cubos_iguais(u, v):
    return u == v and eh_cubo(u) and eh_cubo(v)

#cubo_para_str
def cubo_para_str(cubo):
    n_de_chamada = (0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23)
    cubo = [cor_para_str(cubo[i]) for i in n_de_chamada]
    return linha_curta(cubo[:4]) + linha_longa(cubo[4:-4]) + linha_curta(cubo[-4:])

def linha_curta(part):
    return "      [" + part[0] + "][" + part[1] + "]\n      [" + part[2] + "][" + part[3] + "]"

def linha_longa(part):
    n_de_chamada = (0, 1, 4, 5, 8, 9, 12, 13, 2, 3, 6, 7, 10, 11, 14, 15)
    part = [cor_para_str(part[i]) for i in n_de_chamada]
    return "\n" + linha_pequena(part[:8]) + "\n" + linha_pequena(part[-8:]) + "\n"

def linha_pequena(part):
    if part == []:
        return ""
    else:
        return linha_pequena(part[:-1]) + "[" + part[-1] + "]"

#aplica_sequencia
def aplica_sequencia(cubo, seq):
    for i in simplifica_sequencia(seq):
        cubo = roda_cubo(cubo, i)
    return cubo

#numero_faces_resolvidas
def numero_faces_resolvidas(cubo):
    a = 0
    for i in range(6):
        if cubo[i] == cubo[i + 6] == cubo[i + 12] == cubo[i + 18]:
            a = a + 1
    return a

#esta_resolvido
def esta_resolvido(cubo):
    return numero_faces_resolvidas(cubo) == 6