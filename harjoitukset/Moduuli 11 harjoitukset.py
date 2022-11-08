class Publication:
    def __init__(self,name):
        self.name = name

class Magazine(Publication):
    def __init__(self, name, editor):
        super(). __init__(name)
        self.editor = editor
    def print_info(self):
        print(f"Lehden nimi on:{self.name} päätoimittaja: {self.editor}")

class Book (Publication):
    def __init__(self, author):
        self.author = author
pub1 = Magazine ("Aku Ankka","Aki Hyyppä")
Magazine.print_info()
#pub2 = Publication ("Hytti nro 6")
#pub2.print_info()