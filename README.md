
# Sistema Administrativo de Inventario

Sistema administrativo de inventario con interfaz de línea de comando (CLI). Las instrucciones están proveídas por el programa. Genera reportes de inventario y de movimiento.

Debes crear un usuario para empezar a usarlo.

Descarga el programa en la [sección de releases](https://github.com/e-mts/Inventario/releases/tag/release) o compílalo corriendo build.py.

![image](https://github.com/e-mts/Inventario/assets/61860605/e6755522-424d-4973-b558-bc20c4659b6e)

## Cómo compilar

Puedes encontrar el programa compilado en la [sección de releases](https://github.com/e-mts/Inventario/releases/tag/release) pero si deseas compilarlo tú mismo (ya que es de código abierto), puedes seguir estas instrucciones:

1 - Instala `pyinstaller` desde tu terminal de Python

```
pip install pyinstaller
```

* Si ya tienes `pyinstaller` instalado, puedes verificarlo con
  
  ```
  pip show pyinstaller
  ```

2 - Clona o descarga el repositorio

* Si descargas el repositorio asegúrate de extraerlo del archivo comprimido con el menú contextual (clic derecho) para darle los permisos de usuario correctos.

3 - Abre una terminal con permisos de administrador

4 - Navega hacia el directorio del repositorio desde la terminal

```
cd \direccion\local\de\tu\carpeta
```

5 - Escribe `build.py` en la terminal para correr el script y compilar el programa

6 - El archivo ejecutable se encontrará en la carpeta
