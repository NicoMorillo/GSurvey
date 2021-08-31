def exit_intr_list(name):
    elecc= []
    quest= ("Escribe las opciones para {}: ".format(name))
    x = True
    while x == True:
        term = input(quest)
        if len(elecc) == 2:
            x = False
        if term == "quit":
            break
        elecc.append(term)
    return elecc

def todaslistas():
    a1=exit_intr_list("CCL")
    a2=exit_intr_list("CAS")
    a3=exit_intr_list("CDS")
    eil = a1 + a2 + a3
    return eil

def todojunto(eil):
    print("Lista completa")
    for i, lista in enumerate(eil, 1):
        print("\t {} - {}. ".format(i, lista))
    check= "Todo ok: Y/N"
    if check >= "y":
        return eil
    if check >= "n":
        skills


skills = todaslistas()
skills = todojunto(skills)