from colorama import init, Fore, Style
from alumno_a.funciones import mostrar_menu, ver_tareas, añadir_tarea
from alumno_b.funciones import marcar_completada, eliminar_tarea, despedida

# Menu funcional
numerito = 32
while numerito == 32:
    opcion = mostrar_menu()
        
    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        añadir_tarea()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        despedida()
        numerito += 1
    else:
        print("Opción no válida")