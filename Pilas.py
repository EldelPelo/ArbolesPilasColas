class Pila:
    def __init__(self):
        self.pila = []
    def agregar(self, elemento):
        self.pila.append(elemento)
    def sacar(self):
        if self.vacia()==False:
            return self.pila.pop()
        else:
            return "Pila vacia"
    def vacia(self):
        return self.pila == []

class Pelicula:
    def __init__(self, titulo, protagonista):
        self.titulo = titulo
        self.protagonista = protagonista

def main():
    pila = Pila()
    prot = "Ryan"
    pelicula0 = Pelicula("Deadpool", "Ryan")
    pelicula1 = Pelicula("Figth Club", "Norton")
    pelicula2 = Pelicula("Mr Nobody", "Jared")
    pelicula4 = Pelicula("Deadpool", "Ryan")
    pelicula3 = Pelicula("Terminator", "Arnold")
    pelicula5 = Pelicula("Deadpool", "Ryan")
    pelicula6 = Pelicula("Deadpool", "Ryan")
    pila.agregar(pelicula1)
    pila.agregar(pelicula2)
    pila.agregar(pelicula3)
    pila.agregar(pelicula4)

    while pila.vacia() == False:
        pelicula = pila.sacar()
        if pelicula.protagonista == prot:
            print "Titulo pelicula: " + pelicula.titulo

if __name__ == "__main__":
    main()
