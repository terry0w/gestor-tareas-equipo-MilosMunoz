from colorama import Fore, Style
import os 

def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    # TODO: Implementar

    print(Fore.RED+ "=== GESTOR DE TAREAS ===")
    print(Fore.BLUE+
    '''1. Ver tareas
    2. Añadir tarea
    3. Marcar tarea como completada
    4. Eliminar tarea
    5. Salir'''+Fore.RESET)
    opcion= input("Elige opción: ")

    return opcion

def ver_tareas():
    """Muestra todas las tareas numeradas."""
    # TODO: Implementar
    if not os.path.exists("tareas.txt"):
        with open("tareas.txt", "w", encoding="utf-8") as fichero:
            pass
        print(Fore.RED+f"El fichero {fichero} no existía y ha sido creado")
        print("Cree nuevas tareas para poder verlas"+Fore.RESET)
        return
    
    with open("tareas.txt", "r", encoding="utf-8") as ficheroLeerTareas:
        lineas = ficheroLeerTareas.readlines()
        if not lineas:
            print(Fore.RED+"No hay tareas"+Fore.RESET)
            return
    for i, linea in enumerate(lineas, start=1):
            estado, nombre_tarea = linea.strip().split("|")
            estado_tarea = "[✓]" 
            if estado == "1":
                estado_tarea = "[✓]"
            print(f"{i}. [{estado_tarea}] {nombre_tarea}")
    pass     

def añadir_tarea():
    """Añade una nueva tarea al fichero."""
    # TODO: Implementar
    if not os.path.exists("tareas.txt"):
        with open("tareas.txt", "w", encoding="utf-8") as fichero:
            pass

    with open("tareas.txt","a", encoding="utf-8") as fichero:
        tareaNueva = input("Escriba cual es la nueva tarea que desea añadir a la lista:")
        
        fichero.write("0|"+tareaNueva+"\n")
        print(Fore.GREEN+"tarea añadida con exito"+Fore.RESET)
    pass