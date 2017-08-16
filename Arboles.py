class Nodo():
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der = der

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

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.sacar()
            nodo_izq = pila.sacar()
            pila.agregar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.agregar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)
    


def main():
    exp = raw_input("ingrese l expresion en formato posfijo: ").split(" ")
    pila = Pila()
    convertir(exp, pila)
    print evaluar(pila.sacar())

main()

#Hasta aca hicimos, funciona bien con posfija

class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node


    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)



    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node






    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print (root.data)
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print (root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)
            print (root.data)


def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    print (root)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print ("Traverse Inorder")
    tree.traverseInorder(root)

    print ("Traverse Preorder")
    tree.traversePreorder(root)

    print ("Traverse Postorder")
    tree.traversePostorder(root)


if __name__ == "__main__":
    main()
####################################################################
class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der
class Cola:
    def __init__(self):
        self.cola = []
    def agregar(self, elemento):
        self.cola.append(elemento)
    def sacar(self):
        if self.vacia()==False:
            return self.cola.pop(0)
        else:
            return "Cola vacia"
    def vacia(self):
        return self.cola == []
def evaluar(arbol):
    if(arbol.valor == '+'):
        return evaluar(arbol.izq) + evaluar(arbol.izq)
    if(arbol.valor == '-'):
        return evaluar(arbol.izq) + evaluar(arbol.izq)
    if(arbol.valor == '*'):
        return evaluar(arbol.izq) + evaluar(arbol.izq)
    if(arbol.valor == '/'):
        return evaluar(arbol.izq) + evaluar(arbol.izq)
    return int(arbol.valor)
def crearNodo(valor):
    return Nodo(valor)    
def construirArbol(cadena):
   cola = Cola()
   posicion = 1
   elemento = cadena[posicion]
   raiz = crearNodo(cadena[0])
   while(elemento == '+' or elemento == '-' or elemento == '/' or elemento == '*'):
        cola.agregar(cadena[posicion])
        posicion = posicion + 1
    if(cadena[posicion]!=None):
        cola.agregar(cadena[posicion])
    while(cola.vacia == False):
        
def main():
    string = raw_input()
    cadena = string.split(" ")
    print cadena
if __name__ == "__main__":
    main()

