#2.1 cores
#plano: cores sao de 0 a 5, pois vou poder usar indices diretamnte com cor

cores = ("1", "2", "3", "4", "5", "6")

#cria_cor
def cria_cor(n_cor):
    if n_cor in cores:
        return cores.index(n_cor)
    else:
        raise ValueError("cria_cor: argumentos invalidos")

#eh_cor
def eh_cor(cor):
    return type(cor) is int and cor in range(6)

#cores_iguais
def cores_iguais(v, u):
    return eh_cor(v) and eh_cor(u) and v == u

#cor_para_str
def cor_para_str(cor):
    return cores[cor]

#str_para_cor
def str_para_cor(Str):
    return cria_cor(Str)

#cor_para_int
def cor_para_int(cor):
    return cor + 1

#2.2 movimentos 
#plano: movimentos sao de 0 a 11, assim posso transformar mov em outros com calculos e aritmetica modular e usar mov como indices

movimentos = ("U'", "L'", "F'", "R'", "B'", "D'", "U", "L", "F", "R", "B", "D")
faces = ("U", "L", "F", "R", "B", "D")

#cria_movimento
def cria_movimento(face, sent):
    if face in faces and isinstance(sent, bool):
        return faces.index(face) + (sent * 6)     #como sent tambem eh inteiro, utilizo essa propriedade
    else:
        raise ValueError("cria_movimento: argumentos invalidos")

#obtem_mov_face
def obtem_mov_face(mov):
    return faces[mov % 6]

#obtem_mov_sentido
def obtem_mov_sentido(mov):
    return mov > 5

#eh_movimento
def eh_movimento(mov):
    return type(mov) is int and mov in range(12)

#movimentos_iguais
def movimentos_iguais(mov1, mov2):
    return eh_movimento(mov1) and eh_movimento(mov2) and mov1 == mov2

#movimento_para_str
def movimento_para_str(mov):
    return movimentos[mov]

#str_para_movimento
def str_para_movimento(Str):
    if Str in movimentos[:6]:
        return cria_movimento(Str[0], False)
    elif Str in movimentos[6:]:
        return cria_movimento(Str, True)
    else:
        raise ValueError("str_para_movimento: argumentos invalidos")

#movimento_inverso
def movimento_inverso(mov):
    return (mov + 6) % 12

#str_para_sequencia
def str_para_sequencia(Str):
    return real_str_para_sequencia("S" + Str)       #adicionei o "S" para resolver o problema de se Str[0] = "'"

def real_str_para_sequencia(Str):
    if Str == "S":
        return ()
    elif Str[-1] == "'":
        return real_str_para_sequencia(Str[:-2]) + (str_para_movimento(Str[-2:]),)
    else:
        return real_str_para_sequencia(Str[:-1]) + (str_para_movimento(Str[-1]),)
#teste
#print(str_para_sequencia("U'UFL"))
#print(str_para_sequencia(""))
#print(str_para_sequencia("'"))
#print(str_para_sequencia("UFDK'"))

#sequencia_para_str
def sequencia_para_str(seq):
    if seq == ():
        return ""
    else:
        return sequencia_para_str(seq[:-1]) + movimento_para_str(seq[-1])

#sequencia_inversa
def sequencia_inversa(seq):
    if seq == ():
        return ()
    else:
        return (movimento_inverso(seq[-1]),) + sequencia_inversa(seq[:-1])
#teste
#print(sequencia_inversa((5, 9, 2, 4)))

#simplifica_sequencia
def simplifica_sequencia(seq):      #checa se a seq atual eh igual a simplificacao da seq, se ambas iguais entao nao ha mais partes para simplificar
    if seq == ():
        return ()
    seq_s = algoritmo_simplificar(seq)
    if seq_s == seq:
        return seq
    else:
        return simplifica_sequencia(seq_s)

def atualizar_contador(mov, cont):      #movimentos no sentido horario tem peso 1, e anti horaio 3, pois 3 horarios eh 1 anti horario
    return (cont + (3, 1)[obtem_mov_sentido(mov)]) % 4

def algoritmo_simplificar(seq, contador = 0):
    if len(seq) == 1:
        if contador == 0:
            return seq
        else:
            return ((), ((seq[-1] % 6) + 6,), ((seq[-1] % 6) + 6, (seq[-1] % 6) + 6), (seq[-1] % 6,))[atualizar_contador(seq[-1], contador)]
            #i.e. se seq[-1] eh U entao devolve (nada, U, UU, U') de acordo com o contador (o mesmo eh utilizado na 4a linha apos essa)
    elif seq[-1] % 6 == seq[-2] % 6:
        return algoritmo_simplificar(seq[:-1], atualizar_contador(seq[-1], contador))
    else:
        return algoritmo_simplificar(seq[:-1]) + ((), ((seq[-1] % 6) + 6,), ((seq[-1] % 6) + 6, (seq[-1] % 6) + 6), (seq[-1] % 6,))[atualizar_contador(seq[-1], contador)]
#testes
#print(sequencia_para_str(simplifica_sequencia(str_para_sequencia("FFF'LBU'"))))

#2.3 cubo
#planos: o cubo vai ser um tuple com len(list) = 24, assim todo movimento com o cubo, pode ser descrito por um tuplo com len(tuplo) = 24,
#        e descreve da seguinte forma, o tuplo eh como se foce o novo cubo, mas em vez de dizer logo a cor que esta la, ele diz o indice do cubo antigo
#        de onde esta a cor que ele precisa, i.e para um cubo 1x1x1: [1, 2, 3, 4, 5, 6] x (3, 2, 0, 1, 5, 4) = [4, 3, 1, 2, 6, 5]

def cria_cubo():        #as posicoes de cada face sao tais que sao iguais em mod 6, assim posso acessar por indice
    return (0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5)

#cria_cubo_de_str
def cria_cubo_de_str(Str):
    if isinstance(Str, str) and len(Str) == 24:
        for i in range(24):
            if not Str[i] in cores:
                raise ValueError("cria_cubo_de_str: argumentos invalidos")
        return tuple(cria_cor(Str[i]) for i in (0, 4, 8, 12, 16, 20, 1, 5, 9, 13, 17, 21, 2, 6, 10, 14, 18, 22, 3, 7, 11, 15, 19, 23))
        #transformacao que equivale a minha representacao
    raise ValueError("cria_cubo_de_str: argumentos invalidos")
#testes
#print(cria_cubo_de_str(1))

#cria_copia_cubo
def cria_copia_cubo(cubo):
    return tuple(i for i in cubo)

#obtem_cor_face
def obtem_cor_face(cubo, face):
    if face in faces:
        return tuple(cubo[faces.index(face) + i * 6] for i in range(4))
    else:
        raise ValueError("obtem_cor_face: argumentos invalidos")
#print(obtem_cor_face(cria_cubo(), "U"))

#roda_cubo
#apos tentativas e erros ao fazer esse tuplo de tuplos, nao me sinto orgulhoso com o meu plano, mas veja bem, mais basico o plano => erros mais basicos e efaceis de corrigir :)
transformacoes = (
    #antihorario
    (6, 4, 1, 2, 3, 5, 18, 10, 7, 8, 9, 11, 0, 13, 14, 15, 16, 17, 12, 19, 20, 21, 22, 23),
    (2, 7, 5, 3, 4, 22, 6, 19, 8, 9, 12, 11, 14, 1, 17, 15, 16, 10, 18, 13, 20, 21, 0, 23),
    (0, 1, 8, 11, 4, 7, 6, 18, 20, 9, 10, 19, 3, 13, 2, 5, 16, 17, 15, 12, 14, 21, 22, 23),
    (0, 1, 2, 9, 23, 5, 16, 7, 6, 21, 10, 8, 12, 13, 14, 3, 11, 17, 4, 19, 18, 15, 22, 20),
    (13, 17, 2, 3, 10, 5, 1, 7, 8, 0, 22, 11, 12, 23, 14, 15, 4, 21, 18, 19, 20, 6, 16, 9),
    (0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 23, 12, 14, 15, 16, 13, 5, 18, 20, 21, 22, 19, 17),
    
    #horario
    (12, 2, 3, 4, 1, 5, 0, 8, 9, 10, 7, 11, 18, 13, 14, 15, 16, 17, 6, 19, 20, 21, 22, 23),
    (22, 13, 0, 3, 4, 2, 6, 1, 8, 9, 17, 11, 10, 19, 12, 15, 16, 14, 18, 7, 20, 21, 5, 23),
    (0, 1, 14, 12, 4, 15, 6, 5, 2, 9, 10, 3, 19, 13, 20, 18, 16, 17, 7, 11, 8, 21, 22, 23),
    (0, 1, 2, 15, 18, 5, 8, 7, 11, 3, 10, 16, 12, 13, 14, 21, 6, 17, 20, 19, 23, 9, 22, 4),
    (9, 6, 2, 3, 16, 5, 21, 7, 8, 23, 4, 11, 12, 0, 14, 15, 22, 1, 18, 19, 20, 17, 10, 13),
    (0, 1, 2, 3, 4, 17, 6, 7, 8, 9, 10, 5, 12, 16, 13, 14, 15, 23, 18, 22, 19, 20, 21, 11)
)
#sei que nao testa completamente, ateh porque se testase eu seria capaz de escrever um codigo que fizesse essa tabela por mim ;-;
def goofy_teste_transformacoes(Str):
    for i in range(24):
        if not transformacoes[str_para_movimento(Str)][i] == transformacoes[movimento_inverso(str_para_movimento(Str))].index(i):
            print(False, i)
    return 0
#goofy_teste_transformacoes("U")

def roda_cubo(cubo, mov):
    return tuple(cubo[i] for i in transformacoes[mov])

#eh_cubo
def eh_cubo(cubo):
    if not (isinstance(cubo, (tuple, list)) and len(cubo) == 24):
        return False
    else:
        for i in range(24):
            if not eh_cor(cubo[i]):
                return False
        return True
#testes
#print(eh_cubo(1))

#eh_cubo_valido
def eh_cubo_valido(cubo):
    contador = [0, 0, 0, 0, 0, 0]
    for i in range(24):
        contador[cubo[i]] = contador[cubo[i]] + 1
    return tuple(contador) == (4, 4, 4, 4, 4, 4)

#cubos_iguais
def cubos_iguais(u, v):
    return u == v and eh_cubo(u) and eh_cubo(v)

#cubo_para_str
def cubo_para_str(cubo):
    n_de_chamada = (0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23)
    cubo = tuple(cor_para_str(cubo[i]) for i in n_de_chamada)
    return linha_curta(cubo[:4]) + linha_longa(cubo[4:-4]) + linha_curta(cubo[-4:])

def linha_curta(part):
    return "      [" + part[0] + "][" + part[1] + "]\n      [" + part[2] + "][" + part[3] + "]"

def linha_longa(part):
    n_de_chamada = (0, 1, 4, 5, 8, 9, 12, 13, 2, 3, 6, 7, 10, 11, 14, 15)
    part = [part[i] for i in n_de_chamada]
    return "\n" + linha_pequena(part[:8]) + "\n" + linha_pequena(part[-8:]) + "\n"

def linha_pequena(part):
    if part == []:
        return ""
    else:
        return linha_pequena(part[:-1]) + "[" + part[-1] + "]"

#aplica_sequencia
def aplica_sequencia(cubo, seq):
    if len(seq) == 0:
        return cubo
    else:
        return aplica_sequencia(roda_cubo(cubo, seq[0]), seq[1:])
#testes
#print(cubo_para_str(aplica_sequencia(cria_cubo(), simplifica_sequencia(str_para_sequencia("FF'L'BD")))))

#numero_faces_resolvidas
def numero_faces_resolvidas(cubo):
    contador = 0
    for i in range(6):
        if cubo[i] == cubo[i + 6] == cubo[i + 12] == cubo[i + 18]:
            contador = contador + 1
    return contador

#esta_resolvido
def esta_resolvido(cubo):
    return numero_faces_resolvidas(cubo) == 6 and eh_cubo_valido(cubo)
#testes
#print(cubo_para_str(aplica_sequencia(cria_cubo(), simplifica_sequencia(str_para_sequencia("FFUB")))))

tabela = ("U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'")
def baralha_cubo(cubo, N_mov, seed):
    if eh_cubo(cubo) and type(N_mov, seed) is (int, int) and seed in range(0, 13) and N_mov >= 0:
        return aplica_sequencia(cubo, tuple(tabela[i] for i in gerador_pseudo_aleatorio(N_mov, (seed * 2) % 13)))
    else:
        raise ValueError("baralha_cubo: argumentos invalidos")

def gerador_pseudo_aleatorio(N_mov, seed):
    if N_mov == 0:
        return ()
    return (seed - 1,) + gerador_pseudo_aleatorio(N_mov - 1, (seed * 2) % 13)
#testes
#print(tuple(tabela[i] for i in gerador_pseudo_aleatorio(6, 3))[1:])