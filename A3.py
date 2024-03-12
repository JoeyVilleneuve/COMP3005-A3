from PostgreSQL import *

connection = create_connection("postgres", "postgres", "green6", "127.0.0.1", "5432") # Connect to postgres
query(connection, "CREATE DATABASE a3_101187383") # Create new database
connection = create_connection("a3_101187383", "postgres", "green6", "127.0.0.1", "5432") # Connect to new database

# Insert initial data
query(connection, 
    '''
    CREATE TABLE students (
    student_id SERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE,
    PRIMARY KEY (student_id)
    );

    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    '''
)
    
# getAllStudents: Returns a formatted version of all data in the 'students' table.
def getAllStudents():
    try:
        fetch = queryFetch(connection, "SELECT * FROM students;")
        for row in fetch:
            print("student_id: " + str(row[0])
                + "\nfirst_name: " + str(row[1])
                + "\nlast_name: " + str(row[2]) 
                + "\nemail: " + str(row[3]) 
                + "\nenrollment_date: " + str(row[4]) + "\n"
            )
    except: print("getAllStudents() failed.")
        
# addStudent: Inserts a new student into the 'students' table.
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        query(connection, "INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES ('" + str(first_name) + "','" + str(last_name) + "','" + str(email) + "','" + str(enrollment_date) + "');")
    except: print("addStudent() failed.")

# updateStudentEmail: Updates the email of the student who has the provided student_id.
def updateStudentEmail(student_id, new_email):
    try:
        query(connection, "UPDATE students SET email = '" + str(new_email) + "' WHERE student_id = '" + str(student_id) + "';")
    except: print("updateStudentEmail() failed.")

# deleteStudent: Removes the student who has the provided student_id.
def deleteStudent(student_id):
    try:
        query(connection, "DELETE FROM students WHERE student_id = '" + str(student_id) + "';")
    except: print("deleteStudent() failed.")

# Test cases
getAllStudents()
addStudent('joey', 'villeneuve', 'joeyvilleneuve3@cmail.carleton.ca', '2021-09-01')
getAllStudents()
updateStudentEmail(4, 'wickedcool@hotmail.com')
getAllStudents()
deleteStudent(4)
getAllStudents()