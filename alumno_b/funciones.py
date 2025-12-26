from colorama import Fore, Style

def marcar_completada(fichero):
    """Marca una tarea como completada."""
    # TODO: Implementar
    textoLinea =[]
    with open(fichero,"r", encoding="utf-8") as archivo:

        for numero,linea in enumerate(archivo, start=0):
            linea = linea.strip()
            print(f"{numero}. {linea}")
            textoLinea.append([numero,linea.split("|")])
        numeroTarea = int(input("Ingrese el numero de tarea a marcar: "))
        if len(textoLinea) < numeroTarea+1 or numeroTarea < 0:
            print(Fore.RED+"❌ El número de tarea no existe"+Fore.RESET)
            return

        for nTarea in textoLinea:
            if nTarea[0] == numeroTarea:
                if(nTarea[1][0] == "1"):
                    print(Fore.YELLOW+ "⚠️ La tarea ya esta completa "+Fore.RESET)
                    return
                else:
                    print(nTarea[1][0])
                    nTarea[1][0] = str(1)
                    print(Fore.GREEN+"✅ La tarea se ha completado"+Fore.RESET+"")
    with open(fichero,"w", encoding="utf-8") as archivoEscritura:
        for nTarea in textoLinea:
            print(f"{nTarea[1][0]}|{nTarea[1][1]}", file=archivoEscritura)
    pass

def eliminar_tarea(fichero):
    """Elimina una tarea del fichero."""
    # TODO: Implementar
    textoLinea =[]
    with open(fichero,"r", encoding="utf-8") as archivo:

        for numero,linea in enumerate(archivo, start=0):
            linea = linea.strip()
            print(f"{numero}. {linea}")
            textoLinea.append([numero,linea.split("|")])
        numeroTarea = int(input("Ingrese el numero de tarea a eliminar: "))

        if len(textoLinea) < numeroTarea+1 or numeroTarea < 0:
            print(Fore.RED+"❌ El número de tarea no existe"+Fore.RESET)
            return
        for nTarea in textoLinea:
            if nTarea[0] == numeroTarea:
                tarea_a_borrar = nTarea
        textoLinea.remove(tarea_a_borrar)
        print(textoLinea)
    with open(fichero,"w", encoding="utf-8") as archivoEscritura:
        for nTarea in textoLinea:
            print(f"{nTarea[1][0]}|{nTarea[1][1]}", file=archivoEscritura)
            print(Fore.GREEN+"✅ La tarea se ha borrado correctamente"+Fore.RESET+"")

pass

def despedida():
    """Muestra mensaje de despedida."""
    # TODO: Implementar

    print(Fore.RED+f"NOS{Fore.BLUE} APENA{Fore.RED} QUE YA TE VAYAS\n"
                   f"{Fore.GREEN} HASTA LA PRÓXIMA! {Fore.YELLOW}:D")
    pass