import mysql.connector

# Configuración de conexión (AJUSTA TU PASSWORD AQUÍ)
def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="jerson132007", 
        database="mi_proyecto"
    )

def crud_completo():
    while True:
        print("\n--- SISTEMA CRUD (MySQL + Python) ---")
        print("1. Ver usuarios (Read)")
        print("2. Agregar usuario (Create)")
        print("3. Editar usuario (Update)")
        print("4. Eliminar usuario (Delete)")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            db = obtener_conexion()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM usuarios")
            for u in cursor.fetchall(): print(u)
            db.close()

        elif opcion == "2":
            nombre = input("Nombre del nuevo usuario: ")
            db = obtener_conexion()
            cursor = db.cursor()
            cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (nombre,))
            db.commit()
            print("✅ Guardado.")
            db.close()

        elif opcion == "3":
            id_u = input("ID a editar: ")
            nuevo = input("Nuevo nombre: ")
            db = obtener_conexion()
            cursor = db.cursor()
            cursor.execute("UPDATE usuarios SET nombre = %s WHERE id = %s", (nuevo, id_u))
            db.commit()
            print("🔄 Actualizado.")
            db.close()

        elif opcion == "4":
            id_u = input("ID a eliminar: ")
            db = obtener_conexion()
            cursor = db.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_u,))
            db.commit()
            print("❌ Eliminado.")
            db.close()

        elif opcion == "5":
            break

if __name__ == "__main__":
    crud_completo()