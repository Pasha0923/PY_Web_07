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
            session.query(
                Student.fullname,
                func.round(
                    func.avg(Grade.grade),
                    2
                ).label("avg_grade")
            )
            .select_from(Grade)
            .join(Student)
            .filter(
                Grade.subject_id == subject_id
            )
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .first()
        )

        return result

    finally:
        session.close()