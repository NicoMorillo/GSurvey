skill = []
x = True
control= "Type 'quit' to exit"
print(control)
while x == True:

  term = input("Write a skill: ")
  if term == "quit":
    break

  elif term == " ":
    term= input("Try again: ")
    accep= input("Save: {} \nType y or n ".format(term.title()))
    if accep.lower() >= "y":
      skill.append(term)
    elif accep.lower() >= "n":
      continue

  else:
    accep= input("Save: {} \nType Y/N ".format(term.title()))
    if accep.lower() >= "y":
      skill.append(term)
    elif accep.lower() >= "n":
      continue
    elif accep == "quit":
      break

  if len(skill)== 3:
    x = False

def listado(skill):
  print("This is the skills list: ")
  for i, lista in enumerate(skill, 1):
    print("\t {} {}".format (i, lista.title()))

listado(skill)