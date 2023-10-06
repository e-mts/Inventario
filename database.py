'''
Este script crea la base de datos, crea las tablas y establece las funciones CRUD
'''

import sqlite3

# Creamos una conexión a la base de datos
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Creamos la tabla para la información del producto, las otras tablas hacen referencia a esta
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product_info (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        price REAL,
        quantity INTEGER
    )
''')

# Creamos la tabla para la ubicación de los productos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product_location (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        product_name TEXT,
        location TEXT,
        section TEXT,
        barcode INTEGER,
        FOREIGN KEY (product_name) REFERENCES product_info (name),
        FOREIGN KEY (product_id) REFERENCES product_info (id)
    )
''')

# Creamos la tabla para los movimientos del inventario
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory_movements (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        product_name TEXT,
        movement_type TEXT,
        quantity INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        prod_location TEXT,
        FOREIGN KEY (prod_location) REFERENCES product_location (location),
        FOREIGN KEY (product_id) REFERENCES product_info (id),
        FOREIGN KEY (product_name) REFERENCES product_info (name)
    )
''')

conn.commit()
conn.close()

# Funciones de CRUD
def add_product(name, description, price, quantity, location, section, barcode):
    
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO product_info (name, description, price, quantity)
        VALUES (?, ?, ?, ?)
    ''', (name, description, price, quantity))

    cursor.execute('SELECT * FROM product_info WHERE name = ?', (name,))
    product_info = cursor.fetchone()

    cursor.execute('''
        INSERT INTO product_location (product_id, product_name, location, section, barcode)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_info[0], product_info[1], location, section, barcode))

    movement_type = "Añadido"

    cursor.execute('''
        INSERT INTO inventory_movements (product_id, product_name, movement_type, quantity, prod_location)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_info[0], product_info[1], movement_type, quantity, location))

    conn.commit()
    conn.close()

def display_products():

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT id, name FROM product_info")
    products = cursor.fetchall()

    for product in products:
        product_id, product_name = product
        print(f"ID:{product_id} - {product_name}")

    conn.close()    

def update_product_info(product_id, name, description, price, quantity, location, section, barcode):

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE product_info
        SET name=?, description=?, price=?, quantity=?
        WHERE id=?
    ''', (name, description, price, quantity, product_id))

    cursor.execute('''
        UPDATE product_location
        SET product_name=?, location=?, section=?, barcode=?
        WHERE product_id=?
    ''', (name, location, section, barcode, product_id))

    movement_type = 'Actualizado'

    cursor.execute('SELECT * FROM product_info WHERE id = ?', (product_id,))
    product_info = cursor.fetchone()

    cursor.execute('''
        INSERT INTO inventory_movements (product_id, product_name, movement_type, quantity, prod_location)
        VALUES (?, ?, ?, ?, ?)
    ''', (product_id, name, movement_type, quantity, location))

    conn.commit()
    conn.close()

def delete_product(product_id):

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    movement_type = 'Salida lógica'

    cursor.execute('SELECT * FROM product_info WHERE id = ?', (product_id,))
    product_info = cursor.fetchone()

    cursor.execute('''
        INSERT INTO inventory_movements (product_id, product_name, movement_type)
        VALUES (?, ?, ?)
    ''', (product_info[0], product_info[1], movement_type))

    cursor.execute('DELETE FROM product_location WHERE product_id = ?', (product_id,))
    cursor.execute('DELETE FROM product_info WHERE id = ?', (product_id,))
    
    conn.commit()
    conn.close()

def reduce_product(product_id, quantity):

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    movement_type = 'Salida física'

    cursor.execute('SELECT * FROM product_info WHERE id = ?', (product_id,))
    product_info = cursor.fetchone()

    cursor.execute('''
        INSERT INTO inventory_movements (product_id, product_name, movement_type, quantity)
        VALUES (?, ?, ?, ?)
    ''', (product_info[0], product_info[1], movement_type, quantity - product_info[4]))

    cursor.execute('''
        UPDATE product_info
        SET quantity=?
        WHERE id=?
    ''', (product_info[4] - quantity, product_id))

    print(f"\nCantidad actualizada de producto: {product_info[4] - quantity}")
    
    conn.commit()
    conn.close()

def fetch_product_quantity(product_id):

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM product_info WHERE id = ?', (product_id,))
    product_info = cursor.fetchone()

    product_quantity = product_info[4]

    conn.close()

    return product_quantity