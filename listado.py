from class_dic import job_dic

def listados(name, skill):
    """Display the list of table element"""
    print("This is the list for " + name + ": ")
    for i, lista in enumerate(skill, 1):
        print("\t {} {}".format (i, lista.title()))

def all_skill():
    f_skill = fdic["Skills"]
    s_skill = sdic["Skills"]
    t_skill = tdic["Skills"]
    tod_skill = f_skill + s_skill + t_skill
    return tod_skill

def all_wish():
    f_wish = fdic["Wish"]
    s_wish = sdic["Wish"]
    t_wish = tdic["Wish"]
    tod_wish = f_wish + s_wish + t_wish
    return tod_wish

def all_task():
    f_task = fdic["Task"]
    s_task = sdic["Task"]
    t_task = tdic["Task"]
    tod_task = f_task + s_task + t_task
    return tod_task

f_job = job_dic()
fdic= f_job.crea_cmp_dic()

s_job = job_dic()
sdic= s_job.crea_cmp_dic()

t_job = job_dic()
tdic= t_job.crea_cmp_dic()


#lista_skill = listados("Skill", all_skill())
#lista_wish = listados("Wish", all_wish())
#lista_task = listados("Task", all_task())

