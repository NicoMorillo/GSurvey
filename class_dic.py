class job_dic:
    def __init__(self):
        self.lista_skill=[]
        self.lista_wish=[]
        self.lista_task=[]
        self.count_point= 0
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

        for i in range(1,4):
            Skills = input("Skill {}: ".format(i))
            self.lista_skill.append(Skills)
        dic1["Skills"]= self.lista_skill

        for i in range(1,4):
            Wish = input("Wish {}: ".format(i))
            self.lista_wish.append(Wish)
        dic1["Wish"]= self.lista_wish

        for i in range(1,4):
            Task = input("Task {}: ".format(i))
            self.lista_task.append(Task)
        dic1["Task"]= self.lista_task

        return dic1


#fir = job_dic()
#x = fir.crea_cmp_dic()

#sec= job_dic()
#c = sec.crea_cmp_dic()

#thi= job_dic()
#v= sec.crea_cmp_dic()

