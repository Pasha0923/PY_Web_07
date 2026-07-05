# seed.py

import random

from faker import Faker

from app.db import SessionLocal
from app.models import Group, Teacher, Subject, Student, Grade

fake = Faker()


def seed_database():
    session = SessionLocal()

    try:
        # ======================
        # Создаём группы (3 шт.)
        # ======================
        groups = [
            Group(name="Group A"),
            Group(name="Group B"),
            Group(name="Group C"),
        ]

        session.add_all(groups)
        session.commit()

        # =============================
        # Создаём преподавателей (3-5)
        # =============================
        teachers = [
            Teacher(fullname=fake.name())
            for _ in range(random.randint(3, 5))
        ]

        session.add_all(teachers)
        session.commit()

        # ==========================
        # Создаём предметы (5-8 шт.)
        # ==========================
        subject_names = [
            "Python",
            "Databases",
            "Algorithms",
            "Math",
            "Web",
            "Machine Learning",
            "Statistics",
            "English",
        ]

        selected_subjects = random.sample(
            subject_names,
            k=random.randint(5, 8)
        )

        subjects = [
            Subject(
                name=name,
                teacher=random.choice(teachers)
            )
            for name in selected_subjects
        ]

        session.add_all(subjects)
        session.commit()

        # ============================
        # Создаём студентов (30-50)
        # ============================
        students = [
            Student(
                fullname=fake.name(),
                group=random.choice(groups)
            )
            for _ in range(random.randint(30, 50))
        ]

        session.add_all(students)
        session.commit()

        # ============================
        # Создаём оценки
        # ============================
        grades = []

        for student in students:
            for _ in range(random.randint(10, 20)):
                grade = Grade(
                    student=student,
                    subject=random.choice(subjects),
                    grade=random.randint(50, 100),
                    grade_date=fake.date_between(
                        start_date="-1y",
                        end_date="today"
                    ),
                )
                grades.append(grade)

        session.add_all(grades)
        session.commit()

        print("Database successfully seeded!")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()


if __name__ == "__main__":
    seed_database()