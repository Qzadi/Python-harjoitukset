class Hissi:
    def __init__(self,kerrokset,rappu):
        self.kerrokset = kerrokset
        self.rappu = rappu
        self.kerros_atm = 0


    def kulje(self,kerros):
        self.kerrokset += kerros
        if self.kerrokset >= self.ylin_kerros:
            self.kerrokset = self.ylin_kerros
        if self.kerrokset < 1:
            self.alin_kerros = 1
hissi1 = Hissi (10,1)
hissi1.kulje(9)
