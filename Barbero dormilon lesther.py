#Ejercicio Barbero Dormilon Lesther Zacarías#
# ---------------Menú-------------
print("bienvenido a la barberia Rethsel")
print("Barberia Abierta")
menuprincipal=int(input("menú principal:\n 1- ver estado del barbero \n 0-salir \n "))
while menuprincipal != 0:
    if menuprincipal==1:
        print("barbero dormido")
        barbero=int(input("despertar barbero: \n 1- si  \n 2- no \n ")) 
        while barbero !=0:
              if barbero==1:
                 import threading
                 import time
                 import random
                 import queue 

                 BARBEROS = 1
                 SILLA=1
                 CLIENTES = 9 
                 ASIENTOS = 3
                 ESPERAS = 6 
                 def espera ( ) : 
                      time.sleep ( ESPERAS * random.random ( ) )

                 class Barbero ( threading . Thread ) :
                     condicion = threading . Condition ( ) 
                     alto_completo = threading . Event ( ) 

                     def __init__ ( self , ID ) :
                         super ().__init__()
                         self.ID = ID 


                         def run (self) :
                           while True :
                             try :
                                cliente_actual = sala_espera.get(block=False)
                             except queue . Empty : 
                                 if self.alto_completo.is_set ( ) : 
                                     return

                                 print(f" El barbero {self.ID} está durmiendo ... Zzz ... Zzz ... " )
                                 with self.condicion :
                                     self.condicion.wait ( )
                             else:
                                          cliente_actual.cortar ( self . ID )
                                          
                 class Cliente(threading.Thread):
                     DURACION_CORTE = 5
 
                     def __init__ (self , ID):
                         super () .__init__ ()
                         self.ID = ID
                              
                     def corte (self) : 
                         time.sleep ( self.DURACION_CORTE * random.random () )

                     def cortar ( self , id_barbero ) :
                         print  (f" El barbero {id_barbero} está cortando el cabello del cliente {self.ID}")
                         self.corte ( ) 
                         print (f" El Barbero { id_barbero } terminó de cortar el cabello al cliente { self.ID } " )
                         self.atendido.set ( )    

                     def run ( self ) :
                         self.atendido=threading.Event()

                         try : 
                              sala_espera.put ( self , block = False )
                         except queue . Full : 
                             print (f" La sala de espera está llena , { self.ID } se fue ... " )
                             return

                         print ( f" El cliente { self.ID } se sentó en la sala de espera . " )
                         with Barbero.condicion :
                             Barbero.condicion.notify ( 1 ) 

                         self.atendido.wait ( ) 

 
                 if __name__ == "__main__" :
                     TODOS_CLIENTES = [] 
                     sala_espera = queue . Queue ( ASIENTOS ) 

                     for i in range ( BARBEROS ) : 
                         hilo_barbero = Barbero ( i )
                         hilo_barbero.start ( )

                     for i in range ( CLIENTES ) : 
                         espera ( )
                         cliente = Cliente ( i )
                         TODOS_CLIENTES.append ( cliente )
                         cliente.start ( )

                     for cliente in TODOS_CLIENTES :
                         cliente.join ( )
                                     
                     time.sleep ( 0.1 ) 
                     Barbero.alto_completo.set ( ) 
                     with Barbero.condicion :
                         Barbero.condicion.notify_all ( ) 

                    


         
    

