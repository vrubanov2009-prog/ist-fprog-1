#2.1 cores
#plano: cores sao de 0 a 5, pois vou poder usar indices diretamnte com cor

cores = ("1", "2", "3", "4", "5", "6")

#cria_cor
#checo se eh uma cor, se for, entao transformo na representacao interna
def cria_cor(n_cor):
    """cria_cor: str -> cor
    Recebe um carater '1'..'6' e devolve a cor correspondente.
    Gera ValueError se o argumento nao for valido."""
    if n_cor in cores:
        return cores.index(n_cor)
    else:
        raise ValueError("cria_cor: argumentos invalidos")

#eh_cor
#testo se eh inteiro e se esta no range
def eh_cor(cor):
    """eh_cor: universal -> booleano
    Devolve True se o argumento corresponde a uma cor, e False caso contrario."""
    return type(cor) is int and cor in range(6)

#cores_iguais
#testo se sao cores e em seguida e se os inputs sao iguais
def cores_iguais(v, u):
    """cores_iguais: universal x universal -> booleano
    Devolve True se os dois argumentos sao cores que representam o mesmo digito."""
    return eh_cor(v) and eh_cor(u) and v == u

#cor_para_str
#como disse uso as cores como o index :)
def cor_para_str(cor):
    """cor_para_str: cor -> str
    Devolve o digito ('1' a '6') que identifica a cor."""
    return cores[cor]

#str_para_cor
#reutilizo o cria_cor
def str_para_cor(Str):
    """str_para_cor: str -> cor
    Devolve a cor identificada pelo digito dado.
    Gera ValueError se o digito nao for valido."""
    return cria_cor(Str)

#cor_para_int
#como ja eh um inteiro soh fasso o + 1
def cor_para_int(cor):
    """cor_para_int: cor -> int
    Devolve o inteiro de 1 a 6 que corresponde a cor."""
    return cor + 1

#2.2 movimentos 
#plano: movimentos sao de 0 a 11, assim posso transformar mov em outros com calculos e aritmetica modular e usar mov como indices
#ou seja, em mod 6 obetenho a face do movimento em sentido antihorario

movimentos = ("U'", "L'", "F'", "R'", "B'", "D'", "U", "L", "F", "R", "B", "D")
faces = ("U", "L", "F", "R", "B", "D")

#cria_movimento
#checo se inputs validos, procro pelo .index para conseguir ja um inteiro e para o sentido do movimento aproveito que bool tambem eh int
def cria_movimento(face, sent):
    """cria_movimento: str x booleano -> movimento
    Recebe a face ('U', 'L', 'F', 'R', 'B' ou 'D') e o sentido (True horario,
    False anti-horario) e devolve o movimento correspondente.
    Gera ValueError se os argumentos nao forem validos."""
    if face in faces and isinstance(sent, bool):
        return faces.index(face) + (sent * 6)
    else:
        raise ValueError("cria_movimento: argumentos invalidos")

#obtem_mov_face
#aritmetica modular para desconsiderar que pode ser horario ou antihorario
def obtem_mov_face(mov):
    """obtem_mov_face: movimento -> str
    Devolve a face do movimento."""
    return faces[mov % 6]

#obtem_mov_sentido
#desigualdade de acordo com a separacao que fiz
def obtem_mov_sentido(mov):
    """obtem_mov_sentido: movimento -> booleano
    Devolve True se o movimento eh horario, e False se eh anti-horario."""
    return mov > 5

#eh_movimento
#chacar que eh um int e esta no range, e checar pelo type eh necessario pois se nao eh_movimento(True) => True
def eh_movimento(mov):
    """eh_movimento: universal -> booleano
    Devolve True se o argumento corresponde a um movimento, e False caso contrario."""
    return type(mov) is int and mov in range(12)

#movimentos_iguais
#checo se sao movimentos e se inputs sao iguais
def movimentos_iguais(mov1, mov2):
    """movimentos_iguais: universal x universal -> booleano
    Devolve True se os dois argumentos sao movimentos com a mesma face e sentido."""
    return eh_movimento(mov1) and eh_movimento(mov2) and mov1 == mov2

#movimento_para_str
#uso o movimento como indice
def movimento_para_str(mov):
    """movimento_para_str: movimento -> str
    Devolve a representacao externa do movimento, 'U' ou "U'" por exemplo."""
    return movimentos[mov]

#str_para_movimento
#checo se input valido, e sei que soh eh valido quando esta emm movientos, e uso o .index para conseguir o movimento
def str_para_movimento(Str):
    """str_para_movimento: str -> movimento
    Devolve o movimento correspondente a representacao externa dada.
    Gera ValueError se o argumento nao for valido."""
    if Str in movimentos:
        return movimentos.index(Str)
    else:
        raise ValueError("str_para_movimento: argumentos invalidos")

#movimento_inverso
#aritmetica modular, pois em mod 12, a diferenca entra o movimento e seu inverso eh sempre 6
def movimento_inverso(mov):
    """movimento_inverso: movimento -> movimento
    Devolve o movimento inverso, ou seja, com a mesma face e sentido oposto."""
    return (mov + 6) % 12

#str_para_sequencia
#fiz recurcivamente: f(n) = f(n - 1) + g(n)
def str_para_sequencia(Str):
    """str_para_sequencia: str -> tuplo
    Converte uma string de movimentos, como "L'RUU'", num tuplo de movimentos.
    Gera ValueError se algum dos movimentos nao for valido."""
    if Str == "":      #fim da recursao
        return ()
    elif Str == "'":                        #serve para resolver o problema de se Str == "'", neste caso sem esse elif,
        return str_para_movimento(Str)      #daria sintaxerror pois tentaria acessar Str[-2] que nao existe
    elif Str[-1] == "'":        #discriminar entre horario e antihorario, para aceder e cortar em indices diferentes
        return str_para_sequencia(Str[:-2]) + (str_para_movimento(Str[-2:]),)
    else:
        return str_para_sequencia(Str[:-1]) + (str_para_movimento(Str[-1]),)

#sequencia_para_str
#fiz recurcivamente: f(n) = f(n - 1) + g(n)
def sequencia_para_str(seq):
    """sequencia_para_str: tuplo -> str
    Converte um tuplo de movimentos na sua representacao externa."""
    if seq == ():
        return ""       #fim da recursao
    else:
        return sequencia_para_str(seq[:-1]) + movimento_para_str(seq[-1])

#sequencia_inversa
#fiz recurcivamente: f(n) = g(n) + f(n - 1)
def sequencia_inversa(seq):
    """sequencia_inversa: tuplo -> tuplo
    Devolve a sequencia que desfaz a dada: ordem trocada e cada movimento invertido."""
    if seq == ():
        return ()
    else:
        return (movimento_inverso(seq[-1]),) + sequencia_inversa(seq[:-1])

#simplifica_sequencia
#fiz recurcivamente um checador de se esta simplificado: f(n) => f(g(n)) se n != g(n), onde g(n) eh algoritmo_simplificar
def simplifica_sequencia(seq):
    """simplifica_sequencia: tuplo -> tuplo
    Junta voltas consecutivas da mesma face (modulo 4), repetindo o processo
    aos movimentos que fiquem adjacentes, ate nao haver mais reducoes."""
    if seq == ():
        return ()       #caso especial :[, dava erro ao ter simplifica_sequencia(())
    seq_s = algoritmo_simplificar(seq)
    if seq_s == seq:
        return seq      #fim da recursao
    else:
        return simplifica_sequencia(seq_s)

#movimentos no sentido horario tem peso 1, e anti horaio 3, pois 3 horarios eh 1 anti horario
def atualizar_contador(mov, cont):
    return (cont + (3, 1)[obtem_mov_sentido(mov)]) % 4

#fiz recurcivamente: f(n, x) = f(n - 1, f'(x)) + g(n, x), onde f'(x) eh atualizar_contador e
#                    g(n, x) decide se ira adicionar algo ao resultado e anular o contador, ou continuar contando
def algoritmo_simplificar(seq, contador = 0):
    if len(seq) == 1:                   #if do fim da recursao
        if contador == 0:
            return seq
        else:
            return ((), ((seq[-1] % 6) + 6,), ((seq[-1] % 6) + 6, (seq[-1] % 6) + 6), (seq[-1] % 6,))[atualizar_contador(seq[-1], contador)]
            #i.e. se seq[-1] eh U entao devolve (nada, U, UU, U') de acordo com o contador (o mesmo eh utilizado na 4a linha apos essa)
    elif seq[-1] % 6 == seq[-2] % 6:
        return algoritmo_simplificar(seq[:-1], atualizar_contador(seq[-1], contador))
    else:
        return algoritmo_simplificar(seq[:-1]) + ((), ((seq[-1] % 6) + 6,), ((seq[-1] % 6) + 6, (seq[-1] % 6) + 6), (seq[-1] % 6,))[atualizar_contador(seq[-1], contador)]

#2.3 cubo
#planos: o cubo vai ser um tuple com len(list) = 24, assim todo movimento com o cubo, pode ser descrito por um tuplo com len(tuplo) = 24,
#        e descreve da seguinte forma, o tuplo eh como se foce o novo cubo, mas em vez de dizer logo a cor que esta la, ele diz o indice do cubo antigo
#        de onde esta a cor que ele precisa, i.e para um cubo 1x1x1: [1, 2, 3, 4, 5, 6] x (3, 2, 0, 1, 5, 4) = [4, 3, 1, 2, 6, 5]
#        OBS: nao eh mais um tuplo, pois afinal nao consigo alterar o cubo em baralha_cubo, agora o cubo eh um list :)

#cria_cubo
#as posicoes de cada face sao tais que sao iguais em mod 6, assim posso acessar por indice
def cria_cubo():
    """cria_cubo: {} -> cubo
    Devolve um cubo resolvido."""
    return [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]

#cria_cubo_de_str
#checo os inputs e utilizo um tuple transformador
def cria_cubo_de_str(Str):
    """cria_cubo_de_str: str -> cubo
    Devolve o cubo representado por uma string de 24 digitos ('1' a '6').
    Gera ValueError se o argumento nao for valido."""
    if isinstance(Str, str) and len(Str) == 24:
        for i in range(24):
            if not Str[i] in cores:
                raise ValueError("cria_cubo_de_str: argumentos invalidos")
        return [cria_cor(Str[i]) for i in (0, 4, 8, 12, 16, 20, 1, 5, 9, 13, 17, 21, 2, 6, 10, 14, 18, 22, 3, 7, 11, 15, 19, 23)]
                                          #transformacao que equivale a minha representacao
    raise ValueError("cria_cubo_de_str: argumentos invalidos")

#cria_copia_cubo
#crio uma lista nova com variaveis que nao eh list
#OBS: pouquicimo utilizada pois ja crio cubo novo apos cada funcao que o transforma
#     mas possivelmente util em conjunto com baralha_cubo, caso nao queira baralhar nenhum cubo mas queira a sequencia
def cria_copia_cubo(cubo):
    """cria_copia_cubo: cubo -> cubo
    Devolve uma copia nova do cubo."""
    return [i for i in cubo]

#obtem_cor_face
#checo se inputs validos e uso aritmetica modular mod 6 para aceder as faces
def obtem_cor_face(cubo, face):
    """obtem_cor_face: cubo x str -> tuplo
    Devolve o tuplo das 4 cores da face dada, na ordem de leitura da face.
    Gera ValueError se a face ou o cubo nao forem validos."""
    if face in faces and eh_cubo(cubo):
        return tuple(cubo[faces.index(face) + i * 6] for i in range(4))
    else:
        raise ValueError("obtem_cor_face: argumentos invalidos")

#roda_cubo
#apos tentativas e erros ao fazer esse tuplo de tuplos, nao me sinto orgulhoso com o meu plano
#mas veja bem, mais basico o plano => erros mais basicos e efaceis de corrigir :)
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

#roda_cubo
#transformo o cubo apartir de um tuplo transformador que eh acessado a partir do movimento
def roda_cubo(cubo, mov):
    """roda_cubo: cubo x movimento -> cubo
    Devolve um cubo novo, resultado de aplicar o movimento ao cubo dado."""
    return [cubo[i] for i in transformacoes[mov]]

#eh_cubo
#checo se eh uma lista e se tem len == 24 e se todos os seus componentes sao cores
def eh_cubo(cubo):
    """eh_cubo: universal -> booleano
    Devolve True se o argumento corresponde a um cubo, e False caso contrario."""
    if not (isinstance(cubo, list) and len(cubo) == 24):
        return False
    else:
        for i in range(24):
            if not eh_cor(cubo[i]):
                return False
        return True

#eh_cubo_valido
#criei um contador onde cada cor que eh encontrada eh somado 1 ao respectivo contador da cor se todos derem 4 entao valido
def eh_cubo_valido(cubo):
    """eh_cubo_valido: cubo -> booleano
    Devolve True se cada cor aparece exatamente 4 vezes no cubo."""
    contador = [0, 0, 0, 0, 0, 0]
    for i in range(24):
        contador[cubo[i]] = contador[cubo[i]] + 1
    return tuple(contador) == (4, 4, 4, 4, 4, 4)

#cubos_iguais
#checo se sao cubos e vejo se os inputs sao iguais
def cubos_iguais(u, v):
    """cubos_iguais: universal x universal -> booleano
    Devolve True se os dois argumentos sao cubos com as mesmas cores em todas
    as posicoes."""
    return u == v and eh_cubo(u) and eh_cubo(v)

#cubo_para_str
#isso eh tenebroso, mas basicamente, usei um tuplo transformador para reverter para a notacao externa
#e separo em 3 momentos f(parte1(x)) + g(parte2(x)) + f(parete3(x)), onde f(x) linha_curta e g(x) linha_longa(part)
def cubo_para_str(cubo):
    """cubo_para_str: cubo -> str
    Devolve a rede (planificacao) do cubo, pronta a ser mostrada com print."""
    n_de_chamada = (0, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21, 4, 10, 16, 22, 5, 11, 17, 23)
    cubo = [cor_para_str(cubo[i]) for i in n_de_chamada]
    return linha_curta(cubo[:4]) + linha_longa(cubo[4:-4]) + linha_curta(cubo[-4:])

#equivale as 2 primeiras linhas e 2 ultimas
def linha_curta(part):
    return "      [" + part[0] + "][" + part[1] + "]\n      [" + part[2] + "][" + part[3] + "]"

#uso um tuplo transformador e separo em h(parte2(x)) + h(parte1(x)) onde h(x) eh linha_pequena
def linha_longa(part):
    n_de_chamada = (0, 1, 4, 5, 8, 9, 12, 13, 2, 3, 6, 7, 10, 11, 14, 15)
    part = [part[i] for i in n_de_chamada]
    return "\n" + linha_pequena(part[:8]) + "\n" + linha_pequena(part[-8:]) + "\n"

#equivale a 3a e 4a linha
def linha_pequena(part):
    if part == []:
        return ""
    else:
        return linha_pequena(part[:-1]) + "[" + part[-1] + "]"

#aplica_sequencia
#fiz recurcivamente: f(n, seq) = f(g{n, seq[a]}, seq - 1) onde g(x, y) eh roda_cubo
def aplica_sequencia(cubo, seq):
    """aplica_sequencia: cubo x tuplo -> cubo
    Devolve um cubo novo, resultado de aplicar ao cubo a sequencia de movimentos."""
    if len(seq) == 0:
        return cria_copia_cubo(cubo)        #fim da recursao
        #manter consistencia. em todas as funcoes criei um cubo novo, no caso aplica sequencia(cubo, ()) iria devolver o mesmo sem o cria_copia_cubo
    else:
        return aplica_sequencia(roda_cubo(cubo, seq[0]), seq[1:])

#numero_faces_resolvidas
#de acordo com as regras modulares para as 6 faces checo se os elementos sao iguais entre si, e se sao iguais adiciono 1 no contador
def numero_faces_resolvidas(cubo):
    """numero_faces_resolvidas: cubo -> int
    Devolve o numero de faces do cubo com uma unica cor."""
    contador = 0
    for i in range(6):
        if cubo[i] == cubo[i + 6] == cubo[i + 12] == cubo[i + 18]:
            contador = contador + 1
    return contador

#esta_resolvido
#checo se tem 6 faces resolvidas e se eh um cubo valido, pois se fosse soh 6 faces resolvidas, poderia ter um cubo que nao tinha as 6 cores
def esta_resolvido(cubo):
    """esta_resolvido: cubo -> booleano
    Devolve True se o cubo esta resolvido."""
    return numero_faces_resolvidas(cubo) == 6 and eh_cubo_valido(cubo)

#baralha_cubo
#checo se inputs validos, se validos uso um g(x) que eh o gerador_pseudo_aleatorio para obter a sequencia
#crio um novo_cubo que eh igual ao cubo apos a sequencia, e para cada elemento do cubo inicial, eu equivalo ele ao elemento de mesmo indice do novo cubo
#e isso funciona pois ao passar o cubo pela sequencia eh criado um novo elemento
#dessa forma a lista eh alterada globalmente
tabela = ("U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'")
def baralha_cubo(cubo, N_mov, seed):
    """baralha_cubo: cubo x int x int -> tuplo
    Recebe o numero de movimentos N_mov e uma semente entre 1 e 12, gera N_mov
    movimentos pseudo-aleatorios, aplica-os ao cubo (alterando-o) e devolve o
    tuplo desses movimentos, na ordem em que foram gerados.
    Gera ValueError se os argumentos nao forem validos."""
    if eh_cubo(cubo) and type(N_mov) is int and type(seed) is int and seed in range(1, 13) and N_mov >= 0:
        seq = tuple(str_para_movimento(tabela[i]) for i in gerador_pseudo_aleatorio(N_mov, (seed * 2) % 13))
        novo_cubo = aplica_sequencia(cubo, simplifica_sequencia(seq))
        for i in range(24):
            cubo[i] = novo_cubo[i]
        return seq
    else:
        raise ValueError("baralha_cubo: argumentos invalidos")

#fiz recurcivamente: f(n, seed) = g(seed) + f(n - 1, f'(seed))
#OBS: ao chamar f(n) pela primeira vez, ou seja, no baralha_cubo, a seed ja passa ja passa por um f'(seed)
#     e isso para bater certo com o enunciado
def gerador_pseudo_aleatorio(N_mov, seed):
    if N_mov == 0:
        return ()       #fim da recursao
    return (seed - 1,) + gerador_pseudo_aleatorio(N_mov - 1, (seed * 2) % 13)

#testes
#plano: criar uma funcao testes, onde ha grupos de testes, com cada teste tendo seu proprio numero dentro do grupo, e cada teste ira devolver um bool,
#       True para se passou no teste, e False caso contrario, ao a funcao correr ela ira dar print do seguinte tuple:
#       (numero do grupo, resultado teste 1, ... , resultado teste n)
#       para cada funcao tentei testar os seguintes 3 casos: f(algo valido); f(algo invalido); f(algo valido mas um limite)
#       o f(algo valido mas um limite) eh por exemplo quando tento usar uma sequencia vazia em algo.
#       e isso fiz pois, se alterei algo em algum lugar posso facilmente testar os pontos mais importantes e saber onde esta o erro caso tenha
#       OBS: acabei de alterar testes espero pela ultima, ja que inalizei todas as funcoes, e:
#       1; certos testes nao consegui implementar, entao estao apos a funsao em testes
#       2; me sinto orgulhoso por ter feito inicialmente com tuplos, pois assim todas as funcoes que mudam o cubo, na verdade criam um novo cubo 
#       dessa forma posso criar cubos no inicio e ao usar ele varias vezes, posso sempre chamar o estado inicial :), menos no baralha_cubo :(
#       ai tenho que usar uma copia.

def testes():
    c = cria_cubo()
    F = str_para_movimento("F")
    cubo_bom = cria_cubo_de_str("123456123456123456123456")
    mau = [cria_cor("1")] * 24

    #1; eh_cor, cores_iguais, cor_para_int, cor_para_str, str_para_cor
    t1 = eh_cor(cria_cor("6")) and not eh_cor("0") and not eh_cor(67)
    t2 = cores_iguais(cria_cor("1"), str_para_cor("1")) and not cores_iguais(cria_cor("1"), cria_cor("6")) and not cores_iguais("1", 1)
    t3 = cor_para_int(cria_cor("1")) == 1 and cor_para_int(cria_cor("6")) == 6 and cor_para_str(cria_cor("4")) == "4"
    print(1, t1, t2, t3)

    #2; eh_movimento, movimentos_iguais, obtem_mov_face, obtem_mov_sentido, movimento_para_str, str_para_movimento
    m = str_para_movimento("R'")
    t1 = eh_movimento(cria_movimento("D", True)) and not eh_movimento("D") and not eh_movimento(12)
    t2 = movimentos_iguais(m, cria_movimento("R", False)) and not movimentos_iguais(m, cria_movimento("R", True))
    t3 = obtem_mov_face(m) == "R" and obtem_mov_sentido(m) == False and movimento_para_str(m) == "R'"
    print(2, t1, t2, t3)

    #3; str_para_sequencia, sequencia_para_str, sequencia_inversa, movimento_inverso, simplifica_sequencia
    t1 = str_para_sequencia("") == () and sequencia_para_str(()) == "" and sequencia_inversa(()) == () and simplifica_sequencia(()) == ()
    t2 = sequencia_para_str(simplifica_sequencia(str_para_sequencia("F'B'UU'DDDDBBF"))) == "F'BF"
    t3 = sequencia_para_str(sequencia_inversa(simplifica_sequencia(str_para_sequencia("FDBBBB'B'BU")))) == "U'B'B'D'F'"
    print(3, t1, t2, t3)

    #4; cria_cubo, cria_cubo_de_str, obtem_cor_face, cria_copia_cubo
    t1 = cubos_iguais(cria_cubo_de_str("111122223333444455556666"), c)
    t2 = tuple(cor_para_str(i) for i in obtem_cor_face(cubo_bom, "L")) == ("5", "6", "1", "2")
    t3 = cria_copia_cubo(c) is not c and cubos_iguais(cria_copia_cubo(c), c)
    cop = roda_cubo(c, F)
    t4 = esta_resolvido(c) and not esta_resolvido(cop)
    print(4, t1, t2, t3, t4)

    #5; eh_cubo, eh_cubo_valido, cubos_iguais
    t1 = eh_cubo(c) and eh_cubo(mau) and not eh_cubo("nao e um cubo")
    t2 = not eh_cubo([]) and not eh_cubo(mau[:23]) and not eh_cubo(["1"] * 24)
    t3 = eh_cubo_valido(cubo_bom) and not eh_cubo_valido(mau)
    t4 = not cubos_iguais(c, roda_cubo(c, F)) and not cubos_iguais("67easteregg", "67easteregg")
    print(5, t1, t2, t3, t4)

    #6; roda_cubo, aplica_sequencia
    t1 = tuple(cor_para_str(i) for i in obtem_cor_face(roda_cubo(c, F), "D")) == ("4", "4", "6", "6")
    t2 = cubos_iguais(aplica_sequencia(c, ()), c)
    t3 = cubos_iguais(aplica_sequencia(c, str_para_sequencia("L'RUU'D")), aplica_sequencia(c, str_para_sequencia("L'RD")))
    seq = str_para_sequencia("RUR'U'FDB'L")
    t4 = cubos_iguais(aplica_sequencia(aplica_sequencia(cubo_bom, seq), sequencia_inversa(seq)), cubo_bom)
    print(6, t1, t2, t3, t4)

    #7; numero_faces_resolvidas, esta_resolvido
    t1 = numero_faces_resolvidas(c) == 6 and numero_faces_resolvidas(cubo_bom) == 0 and numero_faces_resolvidas(roda_cubo(c, F)) == 2
    t2 = esta_resolvido(c) and not esta_resolvido(cubo_bom)
    t3 = numero_faces_resolvidas(mau) == 6 and not esta_resolvido(mau)
    print(7, t1, t2, t3)

    #8; baralha_cubo
    t1 = sequencia_para_str(baralha_cubo(cria_cubo(), 5, 3)) == "L'B'BFL" and baralha_cubo(cria_cubo(), 0, 7) == ()
    c2 = cria_cubo()
    t2 = sequencia_para_str(baralha_cubo(c2, 2, 4)) == "R'D" and not cubos_iguais(c2, c)
    t3 = sequencia_para_str(baralha_cubo(cria_cubo(), 1, 1)) == "U'" and sequencia_para_str(baralha_cubo(cria_cubo(), 1, 12)) == "B"
    print(8, t1, t2, t3)
    
    return 0

#esse teste eh mais ou menos pra confirmar se nao fiz um erro de desatencao ao cria a constante transformacoes
#e porque testar dando print do cubo nao eh muito legal:
#1; nao tenho um cubo 2x2, ou seja, confirmar o cubo apos 2 ou mais movimentos eh complicado
#2; como estou limitado a 1 movimento, poderia acontecer o erro de no print estar correto, mas soh estar porque o print nao
#   descrimina entra autocolantes da mesma cor
#sei que nao testa completamente, ateh porque se testase eu seria capaz de escrever um codigo que fizesse essa tabela por mim ;-;
#mas acho que eh o suficiente pois comparo um movimento com o seu inverso, de acordo com uma regra que encontrei, pois eh o inverso
#logo, para estar errado mas passar no teste, devo ter cometido um erro perfeitamente simetrico em amobs, o que acho improvavel, confia.
def goofy_teste_transformacoes():
    for j in faces:
        for i in range(24):
            if not transformacoes[str_para_movimento(j)][i] == transformacoes[movimento_inverso(str_para_movimento(j))].index(i):
                print(False, j, i)
    return 0

#run de testes:



#testes coordenados:

#testes()
#goofy_teste_transformacoes()



#teste independentes:
#testar valluerror

#cria_cor
#n_cor = "12"
#cria_cor(n_cor)

#str_para_cor
#Str = "0"
#str_para_cor(Str)

#cria_movimento
#face = "U"
#sent = 1
#cria_movimento(face, sent)

#str_para_movimento
#Str = "U''"
#str_para_movimento(Str)

#str_para_sequencia
#Str = "'UF'D"
#str_para_sequencia(Str)

#cria_cubo_de_str
#Str = "111122223333444455556667"
#cria_cubo_de_str(Str)

#obtem_cor_face
#cubo = cria_cubo()
#face = "UL"
#obtem_cor_face(cubo, face)

#baralha_cubo
#cubo = cria_cubo()
#N_mov = 5
#seed = True
#baralha_cubo(cubo, N_mov, seed)



#consideracoes finais:
#   acho que tudo funciona bem nos testes independentes deixei as variaveis que devem causar vallueerror de forma sutil,
#   mas tambem corri eles com valores mais basicos.
#   acredito que consegui explicar e implementar bem cada funcao a nao ser por uma parte:
#   problema em aberto:
#   me arrependo da representacao interna de cores e movimentos se intercetar, pois agora passa pela minha cabeca que:
#   eh_movimento(cria_cor("2")) => True ;-;
#   o que sinto que nao deveria acontecer.