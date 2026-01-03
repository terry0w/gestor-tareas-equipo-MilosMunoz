from colorama import Fore, Style

def mostrar_menu():
    """Muestra el menú principal y devuelve la opción elegida."""
    # TODO: Implementar

    print(Fore.RED+ "=== GESTOR DE TAREAS ===")
    print(Fore.BLUE+ '''1. Ver tareas
    2. Añadir tarea
    3. Marcar tarea como completada
    4. Eliminar tarea
    5. Salir'''+Fore.RESET)
    opcion= input("Elige opción: ")

    return opcion

def ver_tareas(fichero):
    """Muestra todas las tareas numeradas."""
    # TODO: Implementar
    pass

def añadir_tarea(fichero):
    """Añade una nueva tarea al fichero."""
    # TODO: Implementar
    pass