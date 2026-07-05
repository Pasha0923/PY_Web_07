from sqlalchemy import (Column,Integer,String,ForeignKey,Date)
from sqlalchemy.orm import (DeclarativeBase,relationship)

class Base(DeclarativeBase):
    pass

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")
    def __repr__(self):
        return f"Student(id={self.id}, fullname='{self.fullname}', group_id={self.group_id})"
class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(150))
    subjects = relationship("Subject", back_populates="teacher")
    def __repr__(self):
        return f"Teacher(id={self.id}, fullname='{self.fullname}')"
    
class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")
    def __repr__(self):
        return f"Subject(id={self.id}, name='{self.name}', teacher_id={self.teacher_id})"
class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    grade_date = Column(Date)
    student_id = Column(Integer,ForeignKey("students.id"))
    subject_id = Column(Integer,ForeignKey("subjects.id"))
    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
    def __repr__(self):
        return f"Grade(id={self.id}, grade={self.grade}, grade_date={self.grade_date}, student_id={self.student_id}, subject_id={self.subject_id})"