from sqlalchemy import func, desc
from app.db import SessionLocal
from app.models import Student, Group, Teacher, Subject, Grade


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    session = SessionLocal()

    try:
        result = (
            session.query(Student.fullname,func.round(func.avg(Grade.grade),2).label("avg_grade"))
            .select_from(Grade).join(Student).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all())
        return result
    finally:
        session.close()

# Знайти студента із найвищим середнім балом з певного предмета.
def select_2(subject_id: int):
    session = SessionLocal()

    try:
        result = (
            session.query(Student.fullname,func.round(func.avg(Grade.grade),2).label("avg_grade"))
            .select_from(Grade).join(Student).filter(Grade.subject_id == subject_id).group_by(Student.id)
            .order_by(desc("avg_grade")).first())
        return result
    finally:
        session.close()

# Знайти середній бал у групах з певного предмета.
def select_3(subject_id: int):
    session = SessionLocal()

    try:
        result = (
            session.query(Group.name,func.round(func.avg(Grade.grade),2).label("avg_grade"))
            .select_from(Grade).join(Student).join(Group).filter(Grade.subject_id == subject_id).group_by(Group.id)
            .all())
        return result
    finally:
        session.close()

# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    session = SessionLocal()
    try:
        result = (session.query(func.round(func.avg(Grade.grade),2)).scalar())
        return result
    finally:
        session.close()

# Знайти які курси читає певний викладач
def select_5(teacher_id: int):
    session = SessionLocal()

    try:
        result = (session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all())
        return result
    finally:
        session.close()

# Знайти список студентів у певній групі.
def select_6(group_id: int):
    session = SessionLocal()

    try:
        result = (session.query(Student.fullname).filter(Student.group_id == group_id).all())
        return result
    finally:
        session.close()

# Знайти оцінки студентів у окремій групі з певного предмета.    
def select_7(group_id: int, subject_id: int):
    session = SessionLocal()

    try:
        result = (session.query(Student.fullname, Grade.grade).join(Grade).filter(Student.group_id == group_id, 
        Grade.subject_id == subject_id).all())
        return result
    finally:
        session.close()

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(teacher_id: int):
    session = SessionLocal()

    try:
        result = (session.query(func.round(func.avg(Grade.grade),2).label("avg_grade"))
        .select_from(Grade).join(Subject).filter(Subject.teacher_id == teacher_id).scalar())
        return result
    finally:
        session.close()

# Знайти список предметів, які відвідує певний студент.
def select_9(student_id: int):
    session = SessionLocal()

    try:
        result = (session.query(Subject.name).join(Grade)
        .filter(Grade.student_id == student_id).distinct().all())
        return result
    finally:
        session.close()

#Список курсів, які певному студенту читає певний викладач.

def select_10(student_id: int, teacher_id: int):
    session = SessionLocal()

    try:
        result = (session.query(Subject.name).join(Grade).join(Subject.teacher)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).distinct().all())
        return result
    finally:
        session.close()

if __name__ == "__main__":
    # print(select_1())
    # print(select_2(8))
    # print(select_3(1))
    # print(select_4())
    # print(select_5(2))
    # print(select_6(1))
    # print(select_7(3,8))
    # print(select_8(3))
    print(select_9(30))
    print(select_10(30,2))