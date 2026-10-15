def simp(seq):
    seq_s = algoritmo_simplificar(seq)
    if seq_s == seq:
        return seq
    else:
        return simp(seq_s)

def algoritmo_simplificar(seq, contador = 0):
    if len(seq) == 1:
        if contador == 0:
            return seq
        else:
            [[], [(seq[-1] % 6) + 6], [(seq[-1] % 6) + 6, (seq[-1] % 6) + 6], [seq[-1] % 6]][contador + (3 - 2 * (seq[-1] // 6))]
    if seq[-1] % 6 == seq[-2] % 6:
        return algoritmo_simplificar(seq[:-1], (contador + (3 - 2 * (seq[-1] // 6))) % 4)
    else:
        return algoritmo_simplificar(seq[:-1]) + [[], [(seq[-1] % 6) + 6], [(seq[-1] % 6) + 6, (seq[-1] % 6) + 6], [seq[-1] % 6]][contador + (3 - 2 * (seq[-1] // 6))]

print(simp(117649))