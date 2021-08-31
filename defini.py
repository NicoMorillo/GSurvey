
def exit_intr_list():
    elecc= []
    quest= "Escribe las opciones: "
    x = True
    while x == True:
        term = input(quest)
        if len(elecc) == 2:
            x = False
        if term == "quit":
            break
        elecc.append(term)
    return elecc
