# Sistema de registro de libros.

def validar_titulo(titulo):
  """Retorna True si el título no está vacío ni es solo espacios."""
  titulo_limpio = titulo.strip()
  if len(titulo_limpio) == 0:
    return False
  return True

def agregar_libro(lista_libros):
  """Solicita datos, valida que no estén vacíos y agrega un nuevo libro."""
  while True:
    titulo = input("Ingrese el título del libro: ")
    if validar_titulo(titulo):
      break 
    print("Error: El título no puede estar vacío ni contener solo espacios.\n")

def validar_copias(copias_str):
  """Retorna True si es un número entero mayor o igual a cero, usando try-except."""
  try:
    valor = int(copias_str)
    if valor >= 0:
      return True
    else:
      return False
  except ValueError:
    return False

def validar_prestamo(prestamo_str):
  """Retorna True si es un número entero mayor a cero, usando try-except."""
  try:
    valor = int(prestamo_str)
    if valor > 0:
      return True
    else:
      return False
  except ValueError:
    return False
  nuevo_libro = {
    "titulo": titulo.strip(),
    "copias": int(copias),
    "prestamo": int(prestamo),
    "disponible": False
  }

  lista_libros.append(nuevo_libro)
  print(f"\nEl libro '{titulo.strip()}' ha sido agregado exitosamente.")

def mostrar_menu():
  """Muestra las opciones del menú en pantalla."""
  print("\n========== MENÚ PRINCIPAL ==========")
  print("1. Agregar libro")
  print("2. Buscar libro")
  print("3. Eliminar libro")
  print("4. Actualizar disponibilidad")
  print("5. Mostrar libros")
  print("6. Salir")
  print("=====================================")

def leer_opcion():
  """Lee la entrada del usuario y valida con try-except que sea un número válido."""
  while True:
    opcion_str = input("Seleccione una opción (1-6): ")
    try:
      opcion = int(opcion_str)
      if 1 <= opcion <= 6:
        return opcion
      else:
        print("Error: Opción fuera de rango. Ingrese un número del 1 al 6.")
    except ValueError:
      print("Error: Entrada inválida. Debe ingresar un número entero.")

def agregar_libro(lista_libros):
  """Solicita datos, valida y agrega un nuevo libro a la colección."""
  titulo = input("Ingrese el título del libro: ")
  copias = input("Ingrese la cantidad de copias: ")
  prestamo = input("Ingrese el período de préstamo en días: ")

  if not validar_titulo(titulo):
    print("Error: El título no puede estar vacío ni contener solo espacios.")
    return

  if not validar_copias(copias):
    print("Error: La cantidad de copias debe ser un número entero mayor o igual que cero.")
    return

  if not validar_prestamo(prestamo):
    print("Error: El período de préstamo debe ser un número entero mayor que cero.")
    return

  nuevo_libro = {
    "titulo": titulo.strip(),
    "copias": int(copias),
    "prestamo": int(prestamo),
    "disponible": False
  }

  lista_libros.append(nuevo_libro)
  print(f"El libro '{titulo.strip()}' ha sido agregado exitosamente.")

def buscar_libro(lista_libros, titulo_buscado):
  """Recorre la lista buscando coincidencias exactas. Retorna la posición o -1."""
  for i in range(len(lista_libros)):
    if lista_libros[i]["titulo"].lower() == titulo_buscado.strip().lower():
      return i
  return -1

def actualizar_disponibilidad(lista_libros):
  """Actualiza el campo 'disponible' en función de la cantidad de copias."""
  for libro in lista_libros:
    if libro["copias"] >= 1:
      libro["disponible"] = True
    else:
      libro["disponible"] = False

def mostrar_libros(lista_libros):
  """Actualiza disponibilidades y muestra todos los registros formateados."""
  actualizar_disponibilidad(lista_libros)
  if not lista_libros:
    print("No hay libros registrados en el sistema.")
    return
  
  print("\n=== LISTA DE LIBROS ===")
  for libro in lista_libros:
    print(f"Título: {libro['titulo']}")
    print(f"Copias: {libro['copias']}")
    print(f"Préstamo: {libro['prestamo']}")
    estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
    print(f"Estado: {estado}")
    print("********************************************")

def main():
  libros = []
  while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
      agregar_libro(libros)
    elif opcion == 2:
      titulo = input("Ingrese el título del libro a buscar: ")
      posicion = buscar_libro(libros, titulo)
      if posicion != -1:
        libro_encontrado = libros[posicion]
        print(f"\nLibro encontrado en la posición {posicion}:")
        print(f"- Título: {libro_encontrado['titulo']}")
        print(f"- Copias: {libro_encontrado['copias']}")
        print(f"- Préstamo (días): {libro_encontrado['prestamo']}")
      else:
        print(f"El libro '{titulo}' no se encuentra registrado.")

    elif opcion == 3:
      titulo = input("Ingrese el título del libro a eliminar: ")
      posicion = buscar_libro(libros, titulo)

      if posicion != -1:
        del libros[posicion]
        print(f"El libro '{titulo}' ha sido eliminado del sistema.")
      else:
        print(f"El libro '{titulo}' no se encuentra registrado.")

    elif opcion == 4:
      actualizar_disponibilidad(libros)
      print("La disponibilidad de todos los libros ha sido actualizada.")

    elif opcion == 5:
      mostrar_libros(libros)

    elif opcion == 6:
      print("Gracias por usar el sistema. Vuelva Pronto")
      break

if __name__ == "__main__":
  main()