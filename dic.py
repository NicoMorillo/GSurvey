arm = {
  'nombre': '',
  'skill': '',
  'wish': '',
  'task': '',
  'texto': ''
}
print(arm.keys())


def crea_dic_key():
  dic1 = {}
  dic1["Job's name: "] = ''
  dic1['Description: '] = ''
  p = 0
  while p != 3:
    z = input("Topics name: ").title()
    dic1[z]= ''
    p += 1
  return dic1

def crea_dicc_value(dic):
  list_topics=[]
  if 1 == len(dic.keys()) or 2 == len(dic.keys()):
      c = input("{}: ".format(x))
      dic[x]= c
  else:
    for x in dic.keys():
        c = input("{}: ".format(x))
        for i in range(3):
            add= input("{}:".format(x))
            list_topics.append(x)
        dic[x] = list_topics
  return dic




