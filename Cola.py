class Cola:
    def __init__(self):
        self.cola = []

    def agregar(self, elemento):
        #print("agrege")
        self.cola.append(elemento)

    def sacar(self):
        if self.vacia()==False:
            return self.cola.pop(0)
        else:
            return "Cola vacia"

    def vacia(self):
        return self.cola == []
    
class Moto:
    def __init__(self,nombre,codigo,placa):
        self.nombre = nombre
        self.codigo = codigo
        self.placa = placa

def main():
    cola = Cola()
    moto0= Moto("Adrian","21312","54as")
    moto1= Moto("Ivan","12342","sa53")
    moto2= Moto("Vargas","12312","sa53")
    moto3= Moto("Pepinosa","34312","sa53")
    moto4= Moto("Paolo","23468","sa53")
    moto5= Moto("Maria","98797","sa53")
    moto6= Moto("Juana","978978","sa53")
    moto7= Moto("Camila","95642","sa53")
    moto8= Moto("Daniela","93130","sa53")
    cola.agregar(moto1)
    cola.agregar(moto0)
    cola.agregar(moto2)
    cola.agregar(moto3)
    cola.agregar(moto4)
    cola.agregar(moto5)
    cola.agregar(moto6)


    while cola.vacia() == False:
        #print "entre"
        moto = cola.sacar()
        
        print "Nombre: " + moto.nombre +"  Codigo: "+moto.codigo+"  Placa: "+moto.placa

 


if __name__ == "__main__":
    main()
