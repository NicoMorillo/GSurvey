

def crea_cmp_dic(self):
    dic1 = {}
    dic1["Job's name: "] = ''
    for x in dic1:
        c = input("Job name: ")
        dic1["Job's name: "] = c
    dic1['Description: '] = ''
    for x in range(1):
        c = input("Job description: ")
        dic1["Description: "] = c
    p = 0

    while p != 3:
        lista_top=[]
        z = input("Topics name: ").title()
        dic1[z]= ''
        for i in range(3):
            c = input("{}: ".format(z))
            lista_top.append(c)
            dic1[z]= lista_top
            lista_top.clear
        p += 1
    return dic1


x = crea_cmp_dic()
c = crea_cmp_dic()
v = crea_cmp_dic