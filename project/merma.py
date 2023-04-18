from db import get_connection

class getAllMerma:
    def getallM():
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call consultar_merma()')
                resulset = curso.fetchall()
            curso.close()
        except Exception as ex:
                print('ERROR')
        return resulset

class searchMerma:
    def searchM(filter):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_merma(%s)',(filter))
                resutset = cursor.fetchall()
                cursor.close()  
        except Exception as ex:
                print('ERROR')
        return resutset

class insertarMerma:
    def insertartM(nombre,cantidad,precioUnidad,idEmpleado):
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call insertar_merma(%s, %s, %s,%s)',
                              (nombre,cantidad,precioUnidad,idEmpleado))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass

