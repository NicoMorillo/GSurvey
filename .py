class omg():
  def __init__(self):
    self.todo = []
    self.toda = []
    self.tabla = []


  def crear(self):
    for i in range(3):
      cuest = input("nombre: ")
      self.tabla.append(cuest)
    return self.tabla

  def arg(self,list):
    for i, c in enumerate(list, 1):
      print("{} - {}".format(i, c))

  def listadelistas(self):
    n_q = int(input("N q: "))
    for x in range(n_q):
      q = "name: "
      q = self.crear()
      self.toda.append(q)
    return self.toda

  def listaconjunta(self):
    n_q = int(input("N q: "))
    for x in range(n_q):
      q = "name: "
      q = self.crear()
      self.todo += q
      self.toda.append(q)
    self.arg(self.todo)

aa= omg()

aa.listaconjunta()
