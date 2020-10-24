class Phone:
    
    def hacer_llamada(self):
        print("Haciendo llamada")
    def jugar(self):
        print("Jugandoooo!")


p1=Phone()
p1.hacer_llamada()
p1.jugar()

##NewClass

class Phone2:
    def add_color(self,color):
        self.color=color
    def add_cost(self,cost):
        self.cost=cost
    def get_color(self):
        return self.color
    def get_cost(self):
        return self.cost



p2=Phone2()
p2.add_color("Verde")
print(p2.get_color())