def cria_cor(n_cor):
    if n_cor in ("1", "2", "3", "4", "5", "6"):
        return int(n_cor)
    else:
        raise ValueError("cria_cor: argumentos invalidos")

def eh_cor(cor_i):
    return cor_i in range(0, 7)

def cores_iguais(v, u):
    return eh_cor(v) and eh_cor(u) and v == u

def cor_para_str(cor_i):
    return str(cor_i)

def cor_para_int(cor_i):
    return cor_i