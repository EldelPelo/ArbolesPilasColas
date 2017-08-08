#LIFO Pilas
pila = [0,1,2,3,4,5,6]
pila.append(7)
print (pila)
print(pila.pop())
print (pila)
#FIFO Colas
from collections import deque
cola = deque([0,1,2])
print(cola)
cola.append(3)
print(cola)
print(cola.popleft())
print(cola)
