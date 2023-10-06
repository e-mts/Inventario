import sqlite3
import openpyxl

# Creamos una conexión a la base de datos
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

def export_inventory_report():

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT t1.*, t2.location, t2.section, t2.barcode
        FROM product_info t1
        INNER JOIN product_location t2 ON t1.name = t2.product_name;
    """)

    products = cursor.fetchall()

    # Creamos un libro de Excel
    excel_filename = "reporte_de_inventario.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active

    # Insertamos los datos al archivo
    ws.append(["Reporte de inventario"]) # type: ignore
    ws.append(["ID", "Nombre", "Cantidad", "Precio", "Ubicación", "Sección", "Código de Barras"]) # type: ignore
    
    for product in products:
        ws.append([product[0], product[1], product[4], product[3], product[5], product[6], product[7]]) # type: ignore

    # Guardamos el archivo
    wb.save(excel_filename)
    print(f"\nReporte de inventario exportado al archivo: {excel_filename}")

    conn.close()

def export_movement_report():

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM inventory_movements')
    movements = cursor.fetchall()

    # Creamos un libro de Excel
    excel_filename = "reporte_de_movimientos.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active

    # Insertamos los datos al archivo
    ws.append(["Reporte de movimientos"]) # type: ignore
    ws.append(["ID", "Nombre", "Movimiento", "Cantidad", "Hora", "Ubicación"]) # type: ignore
    
    for movement in movements:
        ws.append([movement[1], movement[2], movement[3], movement[4], movement[5], movement[6]]) # type: ignore

    # Guardamos el archivo
    wb.save(excel_filename)
    print(f"\nReporte de movimientos exportado al archivo: {excel_filename}")

    conn.close()

def generate_inventory_report():

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT t1.*, (SELECT t2.location FROM product_location t2 WHERE t2.product_name = t1.name) AS location
        FROM product_info t1;
    """)

    products = cursor.fetchall()

    print("\nReporte de inventario:")
    print("=================")
    for product in products:
        print(f"Producto: {product[1]}")
        print(f"Descripción: {product[2]}")
        print(f"Ubicación: {product[5]}")
        print(f"Precio: ${product[3]}")
        print(f"Cantidad: {product[4]}\n")

    conn.close()

    export_flag = input('\n¿Quieres exportar este reporte a un archivo Excel? (y/n): ')

    if export_flag != "y":
        pass
    else:
        export_inventory_report()

def generate_movement_report():

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM inventory_movements')
    movements = cursor.fetchall()

    print("\nReporte de movimientos:")
    print("=================")
    for movement in movements:
        print(f"Producto: {movement[2]}")
        print(f"Movimiento: {movement[3]}")
        print(f"Ubicación: {movement[6]}")
        print(f"Cantidad: {movement[4]}")
        print(f"Hora: {movement[5]}\n")
    
    conn.close()

    export_flag = input('\n¿Quieres exportar este reporte a un archivo Excel? (y/n): ')

    if export_flag != "y":
        pass
    else:
        export_movement_report()
