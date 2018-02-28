class Fila(object):
    """Clase base de fila"""

    def __init__(self):
        """constructor de la clase Fila """
        self.enfila= 0 # Cantidad de personas que 
        self.fila = [] # que tengo en la fila Fila
		       # propiamente, lista vacia

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        
      # Si quiero poner un atributo nuevo o redefinir un atributo
      # heredado de arriba, vuelvo a poner el __init__ y agrego o
      # redefino atributo

      # El "self" en python es para hacer referencia a la misma clase
      # en el caso de cliente en self.dni quiere decir modificar
      # a la misma clase, osea cliente, la modifique poniendo el dni
    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.fila.append(cliente)
        self.enfila += 1

    def atender(self):
        """Atiende al proximo cliente preferencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        pass
    
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.fila.append(cliente)
        self.enfila += 1

    def atender(self):
        """Atiende al proximo cliente General"""
        self.enfila -= 1
        self.fila.pop(0)      

    

class cliente(object):
    """clase cliente """
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria="General"
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria = categoria #agregado FJH
        pass
  
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""

    import random

    nclientes = 1000   
    range_atender = 100
    fg = FilaGeneral() # Como estas clases no tienen atributos
    fp = FilaPreferencial() # iniciales puedo dejar el parentesis vacio
    for i in range(1,nclientes+1):
        random_dni = random.randrange(30000000,33000000)
        random_atender = random.randrange(range_atender)
# ¿Poner otro if para que el loop principal corra sobre un contador que podria ser t
# y decidir si el cliente va a entrar o no e independientemente atienda?
        c = cliente(random_dni)
        random_number = random.randrange(10000)
        if random_number%2 == 0:
            if random_number%7 == 0:
                c.modificarcategoria("Preferencial")
                fp.insertar(c)
#                if random_atender < range_atender*0.7:
#                    fp.atender()   
            else:
                fg.insertar(c)
#                if random_atender < range_atender*0.4:
#                    fg.atender()
        else:
            c.modificarcategoria("Preferencial")
            fp.insertar(c)
#            if random_atender < int(range_atender*0.7):
#                fp.atender()
        if fg.enfila > 0 and random_atender < int(range_atender*0.3):
#             print("atiende general")
            fg.atender()
        if fp.enfila > 0 and random_atender < range_atender*0.6:
            fp.atender()
        print(i,fg.enfila,fp.enfila,fg.enfila+fp.enfila)
