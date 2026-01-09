# gestor-tareas-equipo-MilosMunoz
Crear un proyecto portable de gestión de tareas en Python trabajando en parejas mediante GitHub. Los alumnos aprenderán a configurar entornos virtuales, gestionar dependencias y colaborar en un repositorio compartido utilizando ramas y merges. El proyecto está estructurado en módulos para facilitar el trabajo colaborativo.

# requisitos
python 3.10 + instalar paquetes de requirements.txt


# como instalar 
hacer git clone sobre la url en git
acceder al directorio del gestor desde la terminar
usar $python main.py

# usar aplicacion
la aplicacion es simple y facil de entender usar numeros para las funciones y rellenar los campos como se quiera

# integrantes

Raul Milos
Alonso Muñoz 

# Reglas del Equipo
Siempre hacer *git pull origin main* antes de crear una rama nueva
Siempre hacer *git pull origin main* antes de hacer merge
Cada funcionalidad se desarrolla en una rama separada
Solo se hace merge a main cuando la funcionalidad está completa y probada
El fichero requirements.txt solo se modifica en main
Cada alumno solo modifica los ficheros de su carpeta (excepto el README)

# 1. Asegurarse de estar en main y actualizado
git checkout main
git pull origin main

# 2. Crear una rama nueva para la funcionalidad
git checkout -b nombre-funcionalidad

# 3. Desarrollar y hacer commits
git add .
git commit -m "Descripción del cambio"

# 4. Cuando la funcionalidad esté completa, actualizar main
git checkout main
git pull origin main

# 5. Volver a la rama y hacer merge de main (por si hay cambios)
git checkout nombre-funcionalidad
git merge main

# 6. Si hay conflictos, resolverlos y hacer commit

# 7. Volver a main y hacer merge de la funcionalidad
git checkout main
git merge nombre-funcionalidad

# 8. Subir los cambios a GitHub
git push origin main

# 9. Eliminar la rama local (opcional)
git branch -d nombre-funcionalidad

