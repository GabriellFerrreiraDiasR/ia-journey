def media_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def maior_elemento(lista):
    if len(lista) == 0:
        return None
    return max(lista)

def menor_elemento(lista):
    if len(lista) == 0:
        return None
    return min(lista)