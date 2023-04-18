from db import get_connection

class getAllProveedor:
    def getallPro():
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call mostrar_proveedor()')
                resulset = curso.fetchall()
            curso.close()
        except Exception as ex:
                print('ERROR')
        return resulset
## AUN NO ESTA 
class searchProveedor:
    def searchPro(id):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_proveedor(%s)',(id))
                resutset = cursor.fetchall()
                cursor.close()  
        except Exception as ex:
                print('ERROR')
        return resutset

class insertProveedor:
    def insertPro(nombre,apellidos,matricula,correo):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call insertar_proveedor(%s, %s, %s,%s)',
                              (nombre, apellidos,matricula,correo))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

class modificarProveedor:
    def modificarPro(nombre,apellidos,id,correo):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call modificar_proveedor(%s, %s, %s,%s)',
                              (nombre, apellidos,id,correo))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

class eliminarProveedor:
    def eliminarPro(id):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call eliminar_proveedor(%s)',
                              (id))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

class activarProveedor:
    def activarPro(id):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call activar_proveedor(%s)',
                              (id))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass