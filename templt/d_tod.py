import enum as lis
import dic as ooo


x = lis.deploy



def d_skill(d1, d2, d3):
    """Display the skills and give a point if you select one"""
    x.listados("Skill", x.all_skill())
    for i in range(3):
        c = input("Pick : ")
        if c in ooo.dic1["Skill"]:
            d1 +=1
        if c in ooo.dic2["Skill"]:
            d2 +=1
        if c in ooo.dic3["Skill"]:
            d3 +=1
    return d1, d2, d3

def d_wish(d1, d2, d3):
    """Display the wish and give a point if you select one"""
    x.listados("Wish", x.all_wish())
    for i in range(3):
        c = input("Pick : ")
        if c in ooo.dic1["Wish"]:
            d1 +=1
        if c in ooo.dic2["Wish"]:
            d2 +=1
        if c in ooo.dic3["Wish"]:
            d3 +=1
    return d1, d2, d3


def d_task(d1, d2, d3):
    """Display the task and give a point if you select one"""
    x.listados("Task", x.all_task())
    for i in range(3):
        c = input("Pick : ")
        if c in ooo.dic1["Task"]:
            d1 +=1
        if c in ooo.dic2["Task"]:
            d2 +=1
        if c in ooo.dic3["Task"]:
            d3 +=1
    return d1, d2, d3

def empate(d1, d2, d3):
    """Create a extra question to avoid a equal puntuation"""
    if d1 == d2 and d2 == d3 and d3 == d1 :
        x.listados("Skill", x.all_skill())
        c = input("Extra pick 'pick your favourite one' : ")
        if c in ooo.dic1["Skill"]:
            d1 +=1
        if c in ooo.dic2["Skill"]:
            d2 +=1
        if c in ooo.dic3["Skill"]:
            d3 +=1
    return d1, d2, d3

d1 = 0 
d2 = 0
d3 = 0


p= d_task(d1, d2, d3)
e= d_skill(d1, d2, d3)
q= d_wish(d1, d2, d3)

print(q, e, p)


