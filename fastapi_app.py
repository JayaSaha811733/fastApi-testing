# fastapi_app.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Teacher(BaseModel):
    teacher_id:int
    name:str
    email: str
    ph_number:str
    department:str

teachers: List[Teacher]=[]

class Student(BaseModel):
    student_id:int
    name:str
    email:str
    roll_number:int

students: List[Teacher]=[]



@app.get("/fastapi")
def fastapi():
    return {"message": "Hello from FastAPI!"}

@app.get("/demo")
def fastapi():
    return {"message": "Hello from Jayashree!"}

@app.get("/teacher")
def get_teachers():
    return teachers

@app.post("/teacher")
def add_teacher(teacher: Teacher):
    teachers.append(teacher)
    return teacher

@app.put("/teacher/{teacher_id}")
def update_teacher(teacher_id:int, updated_teacher:Teacher):
    for index, teacher in enumerate(teachers):
        if teacher.id==teacher_id:
            teachers[index]=update_teacher
            return update_teacher
    return {"Error":"Teacher not found" }

@app.delete("/teacher/{teacher_id}")
def delete_teacher(teacher_id:int):
    for index, teacher in enumerate(teachers):
        if teacher.id==teacher_id:
            deleted=teachers.pop(index)
            return deleted
    return {"error": "Teacher not found"}



@app.get("/student")
def get_students():
    return students

@app.post("/student")
def add_student(student: Student):
    students.append(student)
    return student

@app.put("/student/{student_id}")
def update_student(student_id:int, updated_student:Student):
    for index, student in enumerate(students):
        if student.id==student_id:
            students[index]=update_student
            return update_teacher
    return {"Error":"Student not found" }

@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    for index, student in enumerate(teachers):
        if student.id==student_id:
            deleted=students.pop(index)
            return deleted
    return {"error": "Student not found"}


