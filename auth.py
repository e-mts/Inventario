import bcrypt
import sqlite3

# Autenticación de usuarios

# Creamos una conexión a la base de datos
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Creamos una tabla para la información de los usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password_hash TEXT
    )
''')

conn.commit()
conn.close()

# Creamos un Hash de la contraseña para guardar en la base de datos
def hash_password(password):

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Función para verificar la contraseña
def verify_password(input_password, hashed_password):

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

# Insertamos un nuevo usuario en la base de datos
def create_user(username, password):

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, hashed_password))
    conn.commit()

# Proceso para el login
def login(username, password):

    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()
    
    if user_data and verify_password(password, user_data[2]):
        return True  # Login pasó
    else:
        return False  # Login falló