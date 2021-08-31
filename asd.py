from texto_clase import survey

def formato():

    n_topics= int(input("Nº de topics: "))
    n_carrier= int(input("Nº carrier: "))
    todo=[]
    toda=[]
    if n_topics == 1 and n_carrier == 1:
        topic = input("Topic: ")
        topic = survey(topic)

        carrier = input("Carrier : ")
        carrier = topic.exit_intr_list(carrier)
        todo.append(carrier)
        toda += carrier


    else:
        for i in range(n_topics):
            topic= input("Topic: ")
            topic= survey(topic)
            for x in range(n_carrier):
                carrier = input("Carrier : ")
                carrier = topic.exit_intr_list(carrier)
                todo.append(carrier)
                toda += carrier

    return toda
