class Personas:
    def __init__(self) :
        global user, nombre,apellido,cedula,edad,sexo
        nombre=[]
        apellido=[]
        cedula=[]
        edad=[]
        sexo=[]
        user=[]
        
        #Parcial De Brenda Isabel Gaviria Torres Y Jose Angel Cabrales Serrano
    
    def menu(self):
        while True:
            print("\nINGRESASTE MENU PERSONAS")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Personas.agregar())
            elif opcion == "2":
                print(Personas.listar())
            elif opcion == "3":
                print(Personas.eliminar())
            elif opcion =="4":
                print(Personas.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('SELECCIONASTE LA FUNCIONALIDAD AGREGAR')
        nombre=input("ingrese el nombre: ")
        Primer_apellido=input("ingrese apellido: ")
        cc=input("ingrese cedula: ")
        años=input("ingrese edad: ")
        genero=input("ingrese genero: ")
        
        user.append(nombre)
        apellido.append(Primer_apellido)
        cedula.append(cc)
        edad.append(años)
        sexo.append(genero)
        return f'\nagrego el dato',nombre,Primer_apellido,cc,años,genero

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        for i in range(len(user)):
            print(i,user[i])
            print(i,apellido[i])
            print(i,cedula[i])
            print(i,edad[i])
            print(i,sexo[i])
        return f"Lista De Datos Ingresados:",user,apellido,cedula,edad,sexo
    
    def eliminar():
        print('SELECCIONASTE LA FUNCIONALIDAD ELIMINAR')
        nombre_eliminado = input("Ingrese el nombre de la persona a eliminar: ")
        indices_a_eliminar = [i for i in range(len(user)) if user[i] == nombre_eliminado]

        
        for index in sorted(indices_a_eliminar, reverse=True):
            del user[index]
            del apellido[index]
            del cedula[index]
            del edad[index]
            del sexo[index]

        print(f"Se eliminaron todos los datos de {nombre_eliminado}")
        
    def  actualizar():
        print('SELECCIONASTE LA FUNCIONALIDAD ACTUALIZAR')
        print("Datos Actualizados")
        for i in user:
            print(i)

    
class universidades:
    def __init__(self) :
        global unis
        unis=[]
    
    def menu(self):
        while True:
            print("\nINGRESASTE AL MENU UNIVERSIDADES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(universidades.agregar())
            elif opcion == "2":
                print(universidades.listar())
            elif opcion == "3":
                print(universidades.eliminar())
            elif opcion =="4":
                print(universidades.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('SELECCIONASTELA FUNCIONALIDAD AGREGAR')
        uni=input("ingrese la UNiversidad: ")
        unis.append(uni)
        return f'\nagrego el dato',uni

        
    def listar():   
        print('SELECCIONASTE LA FUNCIONALIDAD LISTAR')
        for p in unis:
            print(p)
    
    def eliminar(): 
        print('SELECCIONASTE LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese la universidad a eliminar: ")
        unis.remove(elim)
        print("Dato Eliminado", elim)
        print("Lista Actual", unis)
    
    def  actualizar():
        print('SELECCIONASTE LA FUNCIONALIDAD ACTUALIZAR')
        print("universidades Actualizadas")
        for l in unis:
            print(l)


class restaurantes:
    def __init__(self) :
        global re
        re=[]
    
    def menu(self):
        while True:
            print("\nINGRESASTE AL MENU RESTAURANTES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(restaurantes.agregar())
            elif opcion == "2":
                print(restaurantes.listar())
            elif opcion == "3":
                print(restaurantes.eliminar())
            elif opcion =="4":
                print(restaurantes.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('SELECCIONASTE LA FUNCIONALIDAD AGREGAR')
        r=input("ingrese El Resturante: ")
        re.append(r)
        print("Agregaste El dato ", r)

        
    def listar():   
        print('SELECCIONASTE LA FUNCIONALIDAD LISTAR')
        for p in re:
            print(p)
    
    def eliminar(): 
        print('SELECCIONASTE LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese El Restaurante a eliminar: ")
        re.remove(elim)
        print("Dato Eliminado", elim)
        print("Lista Actual", re)
    
    def  actualizar():
        print('SELECCIONASTE LA FUNCIONALIDAD ACTUALIZAR')
        print("Restaurantes Actualizados")
        for l in re:
            print(l)


class Animales:
    def __init__(self) :
        global ani
        ani=[]
    
    def menu(self):
        while True:
            print("\nINGRESASTE AL MENU ANIMALES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Animales.agregar())
            elif opcion == "2":
                print(Animales.listar())
            elif opcion == "3":
                print(Animales.eliminar())
            elif opcion =="4":
                print(Animales.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('SELECCIONASTE LA FUNCIONALIDAD AGREGAR')
        a=input("ingrese El Animal: ")
        ani.append(a)
        return f'agrego el dato',a

        
    def listar():   
        print('SELECCIONASTE LA FUNCIONALIDAD LISTAR')
        for p in ani:
            print(p)
    
    def eliminar(): 
        print('SELECCIONASTE LA FUNCIONALIDAD ELIMINAR')
        elim=input("ingrese El animal a eliminar: ")
        ani.remove(elim)
        print("Dato Eliminado", elim)
        print("Lista Actual", ani)
    
    def  actualizar():
        print('SELECCIONASTE LA FUNCIONALIDAD ACTUALIZAR')
        print("Animales Actualizados")
        for l in ani:
            print(l)


        
        #return f'Datos Ingresados: ',user
        #return print(user)