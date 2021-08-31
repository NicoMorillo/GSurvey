arm = {
  'nombre': '',
  'skill': '',
  'wish': '',
  'task': '',
  'texto': ''
}
def crea_dic_key():
  dic1 = {}
  dic1['Name'] = ''
  dic1['Texto'] = ''
  p = 0
  while p != 3:
      z = input("nombre de clave: ").title()
      dic1[z]= ''
      p += 1
  return dic1

def crea_dicc_value(dic):
  for x in dic.keys():
    c = input("{}: ".format(x))
    dic[x] = c

#template_dic = crea_dic_key()
#crea_dicc_value(template_dic)


print(arm.keys()[0])