import argparse

from app.db import SessionLocal
from app.crud import (create, list_objects, update, remove)

parser = argparse.ArgumentParser()


parser.add_argument("-a", "--action", required=True, choices=["create","list","update","remove"])
parser.add_argument("-m", "--model", required=True, choices=["Teacher","Group","Student","Subject","Grade"])
parser.add_argument("-id", "--id", type=int, help="ID of the object to update or remove")

# Group , Subject
parser.add_argument("-n", "--name", help="Name of the object (for Group and Subject)")
# Teacher, Student
parser.add_argument("-f", "--fullname", help="Full name of the object (for Teacher and Student)")
# Grade
parser.add_argument("-gr", "--grade", type=int, help="Grade value (for Grade)")

# Foreign Keys
parser.add_argument("-g", "--group_id", type=int, help="Group ID (for Student)")
parser.add_argument("-t", "--teacher_id", type=int, help="Teacher ID (for Subject)")
parser.add_argument("-s", "--student_id", type=int, help="Student ID (for Grade)")
parser.add_argument("-sub", "--subject_id", type=int, help="Subject ID (for Grade)")

args = parser.parse_args()


session = SessionLocal()

try:
    if args.action == "create":
        create(session, args)

    elif args.action == "list":
        list_objects(session, args.model)

    elif args.action == "update":
        update(session,args)

    elif args.action == "remove":
        remove(session,args.model,args.id)

finally:
    session.close()