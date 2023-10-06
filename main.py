import os
from auth import login, create_user
from database import add_product, update_product_info, display_products, delete_product, reduce_product, fetch_product_quantity
from reports import generate_inventory_report, generate_movement_report, export_inventory_report, export_movement_report

def main():

    session = False

    while True:

        os.system('cls')

        print("\nSISTEMA ADMINISTRATIVO DE INVENTARIO")
        user_input = input("\nLista de comandos: \n1 - Iniciar Sesión\n2 - Crear Usuario\n3 - Agregar nuevo producto\n4 - Actualizar información de producto\n5 - Remover producto\n6 - Reportes\n0 - Salir\n\nIngresa un comando: ")
                    
        if user_input == "1":

            if session == True:
                print("\nYa hay una sesión activa.")

            else:
                username = input("\nNombre de Usuario: ")
                password = input("Contraseña: ")

                if login(username, password):
                    print("\nHas iniciado sesión.")
                    session = True

                else:
                    print("\nVerifica tus datos.")
                            
        elif user_input == "2":                        

            username = input("Crea tu nombre de usuario: ")
            password = input("Crea tu contraseña: ")
            create_user(username, password)
            print("\nHas creado un nuevo usuario.")

        elif user_input == "3":

            if session == True:

                pName = input("\nNombre del producto: ")
                pDescription = input("Descripción: ")
                pPrice = input("Precio: $")
                pQuantity = input("Cantidad: ")
                pLocation = input("Ubicación: ")
                pSection = input("Sección: ")
                pBarcode = input("Código de barras: ")
                add_product(pName, pDescription, pPrice, pQuantity, pLocation, pSection, pBarcode)
                print("\nHas agregado un nuevo producto. El movimiento ha sido registrado.")

            else:
                print("\nInicia sesión primero para continuar.")
            
        elif user_input == "4":

            if session == True:
                print("\nLista de productos:")
                display_products()
                pID = input('\nIngresa el ID del producto que quieres modificar: ')
                print("\nIngresa los nuevos detalles del producto")
                pName = input("\nNombre del producto: ")
                pDescription = input("Descripción: ")
                pPrice = input("Precio: $")
                pQuantity = input("Cantidad: ")
                pLocation = input("Ubicación: ")
                pSection = input("Sección: ")
                pBarcode = input("Código de barras: ")
                update_product_info(pID, pName, pDescription, pPrice, pQuantity, pLocation, pSection, pBarcode)
                print("\nHas actualizado una entrada existente. El movimiento ha sido registrado.")

            else:
                print("\nInicia sesión primero para continuar.")

        elif user_input == "5":

            if session == True:

                user_input = input('\n1 - Borrar entrada del inventario\n2 - Restar número de productos en una entrada\n\nSelecciona una opción: ')
                if user_input == '1':
                    print("\nLista de productos:")
                    display_products()
                    pID = input('\nIngresa el ID del producto que quieres borrar: ')
                    delete_product(pID)
                    print("\nHas eliminado una entrada del inventario. (Salida lógica)")
                elif user_input == '2':
                    print("\nLista de productos:")
                    display_products()
                    pID = input('\nIngresa el ID del producto que quieres modificar: ')
                    pActual = fetch_product_quantity(pID)
                    print(f"\nCantidad de producto actual: {pActual}")
                    pQuantity = int(input('\nIngresa la cantidad de producto que salió del inventario: '))
                    reduce_product(pID, pQuantity)
                    print("\nHas reducido el número de productos en la entrada. (Salida física)")

            else:
                print("\nInicia sesión primero para continuar.")

        elif user_input == "6":

            if session == True:
                user_input = input('\n1 - Reporte de inventario\n2 - Reporte de movimientos\n\nSelecciona una opción: ')
                if user_input == '1':
                    generate_inventory_report()
                elif user_input == '2':
                    generate_movement_report()

            else:
                print("\nInicia sesión primero para continuar.")

        else:
            print('\nHasta luego.')
            quit()
                
        another_command = input("\nQuiere ingresar otro comando? (y/n): ").strip().lower()
        if another_command != "y":
            print('\nHasta luego.\n')
            quit()
            
if __name__ == "__main__":
    main()
