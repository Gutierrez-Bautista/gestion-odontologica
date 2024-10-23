import sqlite3

DB_NAME = 'app/clinica.db'

def alta_ficha_general(datos_ficha_general, id_paciente):
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        query = "SELECT * FROM FichaGeneral where id_paciente = ?"
        cursor.execute(query, (id_paciente,))
        valid = cursor.fetchall()
        if not valid:
            cursor.execute('insert into FichaGeneral (id_paciente,obra_social,nro_afiliado,hta,diabetes,alergia,probl_renales,probl_cardiacos,plan_tratamiento,observaciones) values(?,?,?,?,?,?,?,?,?,?)',(id_paciente,*datos_ficha_general))
            valid = cursor.fetchall()
            connection.commit()
            return ['paciente cargado con ficha general','dataUpload',200]
        else: 
            return ['paciente ya cargado', 'dataAlreadyUpload', 200]
    except sqlite3.Error as e:
        return (f"Error al solicitar la información: {e}", "dataBaseError", 500)

def consulta_ficha_general(id_paciente):
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        query = "SELECT * FROM FichaGeneral where id_paciente = ?"
        cursor.execute(query, (id_paciente,))
        valid = cursor.fetchall()

        if valid:
            return ['ficha general del paciente encontrada', valid[0], 200]
        else: 
            return ('paciente no existe','pacienteNotExists',200)
    except sqlite3.Error as e:
        return (f"Error al solicitar la información: {e}", "dataBaseError", 500)

def actualizar_ficha_genral(datos_ficha_general,nombre_apellido):
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        query = "SELECT * FROM FichaPAMI where nombre_apellido = ?"
        cursor.execute(query, (nombre_apellido,))
        valid = cursor.fetchall()
        if not valid:
            cursor.execute('update table FichaGeneral set nombre_apellido = ? ,obra_social = ? ,nro_afiliado = ? ,hta = ? ,diabetes = ? ,alergia,probl_renales = ? ,probl_cardiacos = ? ,plan_tratamiento = ? ,observaciones = ?  where nombre_apellido = ?' , (*datos_ficha_general, nombre_apellido))
            connection.commit()
            valid = cursor.fetchall()
            return ['paciente actualizado con ficha general','dataUpload',200]
        else: 
            return ('paciente no existe','pacienteNotExists',200)
    except sqlite3.Error as e:
        return (f"Error al solicitar la información: {e}", "dataBaseError", 500)