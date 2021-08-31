import dic as dics
class deploy:

    def listados(name, skill):
        """Display the list of table element"""
        print("This is the list for " + name + ": ")
        for i, lista in enumerate(skill, 1):
            print("\t {} {}".format (i, lista))


    def all_skill():
        """Create a list with all items on skill key in a dicctionary"""
        td_skill= dics.dic1["Skill"] + dics.dic2["Skill"] + dics.dic3["Skill"]
        return td_skill

    def all_wish():
        """Create a list with all items on wish key in a dicctionary"""
        td_wish= dics.dic1["Wish"] + dics.dic2["Wish"] + dics.dic3["Wish"]
        return td_wish

    def all_task():
        """Create a list with all items on task key in a dicctionary"""
        td_task= dics.dic1["Task"] + dics.dic2["Task"] + dics.dic3["Task"]
        return td_task


#dp_skill = listados("Skill", all_skill())
#dp_wish = listados("Wish", all_wish())
#dp_task = listados("Task", all_task())

