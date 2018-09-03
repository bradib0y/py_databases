# .create() - creates a new instance all at once
# .select() - finds records in a table
# .save() - updates an existing row in the database
# .get() - finds a single record in a table
# .delete_instance() - deletes a single record from the table
# .order_by() - specify how to sort the records
# if __name__ == '__main__' - a common pattern for making code only run when the script is run and not when it's imported
# db.close() - not a method we used, but often a good idea. Explicitly closes the connection to the database.
# .update() - also something we didn't use. Offers a way to update a record without .get() and .save(). Example: Student.update(points=student['points']).where(Student.username == student['username']).execute()

from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=255, unique = True)
    points = IntegerField(default=0)

    class Meta:
        database = db

students = [
    {'username': "ken", 'points': 9456},
    {'username': "ben", 'points': 5321},
    {'username': "dan", 'points': 7195},
    {'username': "pan", 'points': 9483},
    {'username': "ted", 'points': 2654}
]

def add_students():
    for student in students:
        try:
            Student.create(username = student['username'],
                       points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()
        

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()



