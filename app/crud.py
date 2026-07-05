from datetime import date

from app.models import (Teacher,Group,Student,Subject, Grade)

MODELS = {
    "Teacher": Teacher,
    "Group": Group,
    "Student": Student,
    "Subject": Subject,
    "Grade": Grade,
}

# створити об'єкт певної моделі та додати його до бази даних
def create(session, args):
    model_name = args.model

    if model_name == "Teacher":
        obj = Teacher(fullname=args.fullname)

    elif model_name == "Group":
        obj = Group(name=args.name)

    elif model_name == "Student":
        obj = Student(fullname=args.fullname,group_id=args.group_id)

    elif model_name == "Subject":
        obj = Subject(name=args.name,teacher_id=args.teacher_id)

    elif model_name == "Grade":
        obj = Grade(grade=args.grade,grade_date=date.today(),student_id=args.student_id,
            subject_id=args.subject_id)
    else:
        print(f"Unknown model: {model_name}")
        return

    session.add(obj)
    session.commit()

    print(f"{model_name} created successfully")

# отримати список об'єктів певної моделі 
def list_objects(session, model_name):
    model = MODELS.get(model_name)

    if not model:
        print(f"Unknown model: {model_name}")
        return

    objects = session.query(model).all()

    for obj in objects:
        print(obj)


# оновити об'єкт певної моделі за його ID
def update(session, args):
    model = MODELS[args.model]
    obj = session.get(model, args.id)

    if not obj:
        print(f"{args.model} with id={args.id} not found")
        return

    if args.model in ["Group", "Subject"]:
        if args.name:
            obj.name = args.name
        elif args.fullname:
            print(f"{args.model} doesn't have field 'fullname'")
            return

    elif args.model in ["Teacher", "Student"]:
        if args.fullname:
            obj.fullname = args.fullname
        elif args.name:
            print(f"{args.model} doesn't have field 'name'")
            return

    if args.model == "Student" and args.group_id:
        obj.group_id = args.group_id

    if args.model == "Subject" and args.teacher_id:
        obj.teacher_id = args.teacher_id

    session.commit()
    print(f"{args.model} updated successfully")

# видалити об'єкт певної моделі за його ID
def remove(session, model_name, obj_id):
    model = MODELS.get(model_name)

    if model is None:
        print(f"Unknown model: {model_name}")
        return

    obj = session.get(model, obj_id)

    if obj is None:
        print("Object not found")
        return

    session.delete(obj)
    session.commit()

    print(f"{model_name} deleted successfully")