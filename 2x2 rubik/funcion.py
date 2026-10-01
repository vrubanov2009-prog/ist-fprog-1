def simple(a):
    return 1

def translate_in(a):
    b = extend(a)
    c = str(count(b))
    return (no_repeat(b, c), c)

def extend(a):
    if len(a) == 0:
        return ""
    if len(a) == 1:
        return a
    if a[-1] == "'":
        return extend(a[:-2]) + a[-2] + a[-2] + a[-2]
    return extend(a[:-1]) + a[-1]

def count(a):
    if len(a) == 1:
        return 1
    if a[-1] == a[-2]:
        return 1 + count(a[:-1])
    return 1 + (count(a[:-1]) * 10)

def no_repeat(a, b):
    if len(a) == 0:
        return ""
    return a[0] + no_repeat(a[int(b[0]):], b[1:])

i = input()
a = translate_in(i)
print(a)