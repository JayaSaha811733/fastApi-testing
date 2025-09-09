# fastapi_app.py
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()
router=APIRouter

DATABASE_URL="sqlite:///./test.db"

engine=create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    ph_number = Column(String, index=True)
    department = Column(String, index=True)
Base.metadata.create_all(bind=engine)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



class CreateTeacher(BaseModel):
    # teacher_id:int
    name:str
    email: str
    ph_number:str
    department:str

class TeacherResponse(BaseModel):
    teacher_id:int
    name:str
    email:str

    class config:
        orm_mode=True

# teachers: List[Teacher]=[]

class TeacherUpdate(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    ph_number:Optional[str]=None
    department:Optional[str]=None
    



@app.post("/teachers/", response_model=TeacherResponse)
def create_Teacher(teacher:CreateTeacher, 
db: Session = Depends(get_db)):
    db_teacher=Teacher(
        name=teacher.name, 
        email=teacher.email,
        ph_number=teacher.ph_number,
        department=teacher.department
        )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher



@app.get('/teachers/', response_model=List[TeacherResponse])
def read_teachers(skip: int=0, limit: int = 10, db:Session=Depends(get_db)):
    teachers=db.query(Teacher).offset(skip).limit(limit).all()
    return teachers

@app.get('/teachers/{teacher_id}', response_model=TeacherResponse)
def read_teachers(teacher_id:int, db:Session=Depends(get_db)):
    teacher=db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="User not found")
    return teacher

@app.put("/teachers/{teacher_id}", response_model=TeacherResponse)
def update_teachers(teacher_id: int, teacher: TeacherUpdate, db:Session=Depends(get_db) ):
    db_teacher= db.query(Teacher).filter(Teacher.teacher_id==teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_teacher.name=teacher.name if teacher.name is not None else db_teacher.name
    db_teacher.email=teacher.email if teacher.email is not None else db_teacher.email
    db_teacher.ph_number=teacher.ph_number if teacher.ph_number is not None else db_teacher.ph_number
    db_teacher.department=teacher.department if teacher.department is not None else db_teacher.department
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


@app.delete("/teachers/{teacher_id}", response_model=TeacherResponse)
def delete_teachers(teacher_id: int, db:Session=Depends(get_db)):
    db_teacher=db.query(Teacher).filter(Teacher.teacher_id==teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_teacher)
    db.commit()
    return db_teacher





class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    ph_number = Column(String, index=True)
    course=Column(String, index=True)



class CreateStudent(BaseModel):
    name:str
    email:str
    ph_number:str
    course:str

class StudentResponse(BaseModel):
    student_id:int
    name:str
    email:str
    ph_number:str
    course:str

    class config:
        orm_mode=True

# teachers: List[Teacher]=[]

class StudentUpdate(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    ph_number:Optional[str]=None
    course:Optional[str]=None




@app.post("/students/", response_model=StudentResponse)
def create_students(student:CreateStudent, 
db: Session = Depends(get_db)):
    db_student=Student(
        name=student.name, 
        email=student.email,
        ph_number=student.ph_number,
        course=student.course
        )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student



@app.get('/students/', response_model=List[StudentResponse])
def read_students(skip: int=0, limit: int = 10, db:Session=Depends(get_db)):
    students=db.query(Student).offset(skip).limit(limit).all()
    return students

@app.get('/students/{student_id}', response_model=StudentResponse)
def read_students(student_id:int, db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.student_id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="User not found")
    return student

@app.put("/students/{students_id}", response_model=StudentResponse)
def update_students(student_id: int, student: StudentUpdate, db:Session=Depends(get_db) ):
    db_student= db.query(Student).filter(Student.student_id==student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_student.name=student.name if student.name is not None else db_student.name
    db_student.email=student.email if student.email is not None else db_student.email
    db_student.ph_number=student.ph_number if student.ph_number is not None else db_student.ph_number
    db_student.course=student.course if student.course is not None else db_student.course
    db.commit()
    db.refresh(db_student)
    return db_student


@app.delete("/teachers/{teacher_id}", response_model=TeacherResponse)
def delete_teachers(teacher_id: int, db:Session=Depends(get_db)):
    db_teacher=db.query(Teacher).filter(Teacher.teacher_id==teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_teacher)
    db.commit()
    return db_teacher




@app.get("/fastapi")
def fastapi():
    return {"message": "Hello from FastAPI!"}

@app.get("/demo")
def fastapi():
    return {"message": "Hello from Jayashree!"}

# @app.get("/teacher")
# def get_teachers():
#     return teachers

# @app.post("/teacher")
# def add_teacher(teacher: Teacher):
#     teachers.append(teacher)
#     return teacher

# @app.put("/teacher/{teacher_id}")
# def update_teacher(teacher_id:int, updated_teacher:Teacher):
#     for index, teacher in enumerate(teachers):
#         if teacher.id==teacher_id:
#             teachers[index]=update_teacher
#             return update_teacher
#     return {"Error":"Teacher not found" }

# @app.delete("/teacher/{teacher_id}")
# def delete_teacher(teacher_id:int):
#     for index, teacher in enumerate(teachers):
#         if teacher.id==teacher_id:
#             deleted=teachers.pop(index)
#             return deleted
#     return {"error": "Teacher not found"}



# @app.get("/student")
# def get_students():
#     return students

# @app.post("/student")
# def add_student(student: Student):
#     students.append(student)
#     return student

# @app.put("/student/{student_id}")
# def update_student(student_id:int, updated_student:Student):
#     for index, student in enumerate(students):
#         if student.id==student_id:
#             students[index]=update_student
#             return update_teacher
#     return {"Error":"Student not found" }

# @app.delete("/student/{student_id}")
# def delete_student(student_id:int):
#     for index, student in enumerate(teachers):
#         if student.id==student_id:
#             deleted=students.pop(index)
#             return deleted
#     return {"error": "Student not found"}


