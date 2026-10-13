def cria_cor(n_cor):
    if n_cor in ("1", "2", "3", "4", "5", "6"):
        return int(n_cor)
    else:
        raise ValueError("cria_cor: argumentos invalidos")

def eh_cor(cor_i):
    if cor_i in (1, 2, 3, 4, 5, 6):
        return True
    else:
        return False

def cores_iguais(v, u):
    if eh_cor(v) and eh_cor(u) and u == v:
        return True
    return False

def cor_para_str(cor_i):
    return str(cor_i)

def cor_para_int(cor_i):
    return cor_i