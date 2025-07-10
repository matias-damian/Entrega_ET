# Nombre: Matias Damian Toledo del Solar
# Rut: 21.634.543-6
# Fecha: 10-07-2025
# Asignatura: Fundamentos de Programación 002D

# Inicialización de variables
productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["Acer", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "12GB", "DD", "1T", "Intel Core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "12GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "123FHD": ["Acer", 15.6, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["Acer", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"]
}

stock = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 4],
    "JjfFHD": [424990, 1],
    "fgdxFHD": [664990, 21],
    "GF75HD": [749990, 2],
    "123FHD": [290890, 32],
    "342FHD": [444990, 7],
    "UWU131HD": [349990, 1]
}

# Funciones
def stock_marca(marca: str) -> None:
    marca = marca.lower()
    total_stock = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca and modelo in stock:
            total_stock += stock[modelo][1]
    
    if total_stock == 0:
        print("Marca no encontrada/sin stock")
    else:
        print("*** STOCK ***")
        print(f"Marca: {marca}")
        print(f"Stock: {total_stock}")

def busqueda_precio(p_min: int, p_max: int) -> None:
    if p_min > p_max:
        print("El precio mínimo no puede ser mayor al precio máximo")
        return
    
    print("*** BUSQUEDA POR PRECIO ***")
    resultados = []
    for modelo, stock_info in stock.items():
        if p_min <= stock_info[0] <= p_max and stock_info[1] > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")
    
    if not resultados:
        print("No hay notebooks en ese rango de precios.")
    else:
        resultados.sort()
        for resultado in resultados:
            print(resultado)

def eliminar_producto(marca: str) -> bool:
    marca = marca.lower()
    modelos_a_eliminar = [modelo for modelo, datos in productos.items() if datos[0].lower() == marca]
    
    if not modelos_a_eliminar:
        return False
    
    for modelo in modelos_a_eliminar:
        productos.pop(modelo, None)
        stock.pop(modelo, None)
    
    return True

def caso_eliminar_producto() -> None:
    while True:
        modelo = input("Ingrese el modelo a eliminar (no distingue mayúsculas ni minúsculas): ").lower()
        if eliminar_producto(modelo):
            print("Producto eliminado!!")
        else:
            print("El modelo no existe!!")
        
        eliminar_mas = input("¿Desea eliminar otro producto? (si/no): ").lower()
        if eliminar_mas != "si":
            break

# Menú principal
def menu() -> None:
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Eliminar producto.")
        print("4. Salir")

        try:
            opcion = int(input())
        except ValueError:
            print("Debe ingresar una opción válida!!")
            continue

        if opcion == 1:
            marca = input("Ingresa la marca (no distingue mayúsculas ni minúsculas): ").lower()
            stock_marca(marca)
        elif opcion == 2:
            try:
                p_min = int(input("Ingrese el precio mínimo: "))
                p_max = int(input("Ingrese el precio máximo: "))
            except ValueError:
                print("Debe ingresar números enteros!!")
                continue
            busqueda_precio(p_min, p_max)
        elif opcion == 3:
            caso_eliminar_producto()
        elif opcion == 4:
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar una opción válida!!")

menu()
