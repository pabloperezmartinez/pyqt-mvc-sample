from models.db_conector import DatabaseConnection

class StudentModel:
    def __init__(self) -> None:
        db = DatabaseConnection()
        self._conn = db.connection
        self._cur = db.cursor
    
    def get_students(self):
        query = "SELECT * FROM students ORDER BY last_name"
        self._cur.execute(query)
        return self._cur.fetchall()
    
    def create_student(self, first_name, last_name, email):
        query = "INSERT INTO students (first_name, last_name, email) VALUES (%s,%s,%s)"
        self._cur.execute(query, (first_name, last_name, email))
        self._conn.commit()
        
    def update_student(self, student_id, first_name, last_name, email):
        try:
            query = "UPDATE students SET first_name=%s, last_name=%s, email=%s WHERE id=%s"
            self._cur.execute(query,(first_name,last_name,email,student_id))
            self._conn.commit()
            return True
        except Exception as e:
            print (f"¡Explotó el programa!: {str(e)}")
            
    def delete_student(self, student_id):
        try:
            query = "DELETE FROM students WHERE id=%s"
            self._cur.execute(query,(student_id,))
            self._conn.commit()
        except Exception as e:
            print (f"¡Explotó el programa!: {str(e)}")
            
    def get_student_by_id(self, student_id):
        try:
            query = "SELECT * FROM students WHERE id = %s"
            self._cur.execute(query, (student_id,))
            return self._cur.fetchone()
        except Exception as e:
            print(f"Error al obtener el estudiante: {str(e)}")
            return None