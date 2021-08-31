from class_dic import job_dic
from listado import listados

f_job = job_dic()
s_job = job_dic()
t_job = job_dic()

fdic= f_job.crea_cmp_dic()
sdic= s_job.crea_cmp_dic()
tdic= t_job.crea_cmp_dic()

f_skill = fdic["Skills"]
s_skill = sdic["Skills"]
t_skill = tdic["Skills"]

f_wish = fdic["Wish"]
s_wish = sdic["Wish"]
t_wish = tdic["Wish"]

f_task = fdic["Task"]
s_task = sdic["Task"]
t_task = tdic["Task"]


tod_skill = f_skill + s_skill + t_skill
tod_wish = f_wish + s_wish + t_wish
tod_task = f_task + s_task + t_task 

lista_skill = listados("Skill", tod_skill)
lista_wish = listados("Wish", tod_wish)
lista_task = listados("Task", tod_task)