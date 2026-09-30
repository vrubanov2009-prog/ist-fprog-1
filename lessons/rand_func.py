def str_swap(a):
    if len(a)==0:
        return("")
    return(a[-1]+str_swap(a[:-1]))
print(str_swap(input()))