import os
os.system("cls")

listatipo=[""]*100
listanombre=[""]*100
listarut=[""]*100
listapeso=[0.0]*100
listaprecio=[0]*100
listaciudad=[""]*100

def menu():
    print("""
    1-Grabar
    2-Buscar
    3-Listar encomiendas
    4-SALIR
    """)

def grabar(n,i):
    if n==1:
        print("ingrese los datos de la encomienda\n")
    while True:
        listatipo[i]=input("sobre o paquete")  
        if listatipo[i]=="sobre" or listatipo[i]=="paquete":
            break
        else:
            print("Debe ser sobre o paquete")

    while True:
        listanombre[i]=input("nombre destinatario")
        nombre=len(listanombre[i])
        if nombre>=2 and nombre<=30:
            break
        else:
            print("nombre no valido")
        
        listarut[i]=input("rut destinatario")
    while True:
        try:
            listapeso[i]=float(input("peso en kg"))
            if listapeso[i]>=0.1:
                break
            else:
                print("Debe ser mayor a 0.1kg")
        except:
            print("Error de Dato")
    while True:
        try:
            listaprecio[i]=int(input("precio"))
            if listaprecio[i]>=2000:
                break
            else:
                print("Debe ser como minimo $2000")
        except:
            print("Error de Dato")
    while True:
        listaciudad[i]=input("ciudad de destino")
        x=len(listaciudad[i])
        if x>=3:
            break
        else:
            print("Debe de tener como minimo 3 caracteres")        

def imprimir(cont):
    sobre=0
    paquete=0
    for j in range (cont):
        print("encomienda")
        print("tipo\tnombre\trut\tpeso\tprecio\ttipo\t")
        print(listatipo[j],end='\t')
        print(listanombre[j],end='\t')
        print(listarut[j],end='\t')
        print(listapeso[j],end='\t')
        print(listaprecio[j],end='\t')
        print(listaciudad[j])
        if listatipo[j]=="sobre":
            sobre+=1
        elif listatipo[j]=="paquete":
            paquete+=1
    print(f"cantidad de sobres={sobre}, cantidad de paquete={paquete}")
def buscar(r):
    l=0
    for i in range (len(listarut)):
        if listarut[i]==r:
            print("tipo\tnombre\tpeso\tprecio\ttipo\t")
            print(listatipo[i],end='\t')
            print(listanombre[i],end='\t')
            print(listapeso[i],end='\t')
            print(listaprecio[i],end='\t')
            print(listaciudad[i])
            l=1
        if l==0:
            print("Rut no encontrado")

cont=0
i=0
while True:   
    try:
        menu()
        n=int(input("Seleccione una opcion  "))
        if n==4:
            print("ADIOS")
            break
        elif n==1:
            grabar(n,i)
            cont=cont+1
            i=i+1
        elif n==2:
            r=input("ingrese el rut a buscar  ")
            buscar(r)
        elif n==3:
            if cont==0:
                print("No existen encomiendas")
            else:
                imprimir(cont)
        else:
            print("Opcion del menu no valida")

    except:
        print("Error de Dato")

