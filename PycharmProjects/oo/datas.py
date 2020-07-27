class Data: #class é como uma receita, define as características do objeto
    def __init__(self, dia, mes, ano): #def é para definir uma função, já o __init__(self) é o início da construção do objeto
        self.dia = dia #é necessário acessar a váriavel através do self.
        self.mes = mes
        self.ano = ano

    def formatada(self):
        (print(self.dia,"/",self.mes,"/",self.ano))
