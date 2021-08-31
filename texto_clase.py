import random

class survey:
    def __init__(self, tipe):
        self.tipe = tipe

    def exit_intr_list(self, name):
        quest= ("Write the {} for {}: ".format(self.tipe, name))
        lista=[]
        x = True
        while x == True:
            term = input(quest)
            if len(lista) == 2:
                x = False
            if term == "quit":
                break
            lista.append(term.title())
        return lista

    def todaslistas(self):
        sa = skills.exit_intr_list("sa")
        devp = skills.exit_intr_list("devp")
        soa = skills.exit_intr_list("soa")
        options = sa + devp + soa
        random.shuffle(options)
        return options

    def todojunto(self, lista):
        print("Complete list")
        for i, linea in enumerate(lista, 1):
            print("\t {} - {}. ".format(i, linea))


#skills = survey("skills")
#listt = skills.todaslistas()
#skills.todojunto(listt)
