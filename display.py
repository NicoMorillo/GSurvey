import listado as lip
from class_dic import job_dic

print("Van a aparecer las tres listas: elige 3 ")
count_point = 0


lista_skill = lip.listados("Skill", lip.all_skill())
for q in range(1,4):
    c= input("Skill {}:  ".format(q)).title()
    if c == lip.f_dic:
        print("punto")



    #lista_wish = lip.listados("Wish", lip.all_wish())
    #c= input("la primera es?? : ")


    #lista_task = lip.listados("Task", lip.all_task())
    #c= input("la primera es?? : ")

