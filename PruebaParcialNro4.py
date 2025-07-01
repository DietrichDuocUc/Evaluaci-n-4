







#def menu_totem():

while True:
    
    print("""TOTEM AUTOATENCIÓN RESERVA STRIKE
    1.- Reservar zapatillas
    2.- Buscar zapatillas reservadas.
    3.- Cancelar reserva de zapatillas.
    4.- Salir.""")
    
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print(Reservar_zapatillas)
    elif opcion == "2":
        print(Buscar_zapatillas)
    elif opcion == "3":
        print(Cancelar_reserva)
    elif opcion == "4":
        print("Programa terminado...")
        break   
    else: 
        print("Debe ingresar una opción válida!!")
print("Programa terminado...")        
        
        
        
#def Reservar_zapatillas():



lista_nombres = ["Estela Perez","Juan Solis","Guillermo Pinto"]
lista_zapatillas = ["estándar", "plus", "low"]


    """-- Reservar Zapatillas --
Nombre del comprador: Estela Perez
Digite la palabra secreta para confirmar la reserva: EstoyEnListaDeReserva
Reserva realizada exitosamente para Estela Perez."""

#def Buscar_zapatillas():   

"""-- Buscar Zapatillas Reservadas --
Nombre del comprador a buscar: Estela Perez
Reserva encontrada: Estela Perez - 1 par(es) (estándar).
¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): s
Reserva actualizada a VIP. Ahora Estela Perez tiene 2 pares reservados
"""

#def Cancelar_reserva():  

"""-- Cancelar Reserva --
Nombre del comprador cuya reserva desea cancelar: Guillermo Pinto
La reserva de Guillermo Pinto ha sido cancelada.
"""          