from sqlalchemy import insert
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Tag, Task

engine = create_engine('sqlite:///todos.db')
Session = sessionmaker(bind=engine)
session = Session()


class query_todo():
    
    def create(todo):
            task = Task(title=todo[0], description=todo[1], category_id=todo[2], tag_id=todo[3])
            session.add(task)
            session.commit()

    def fetch_all():
          tasks= session.query(Task)
          task_table=[]

          for task in tasks:
                task_id=str(task.id)
                task_title=task.title
                task_description=task.description
                task_category=str(task.category_id)
                task_tag=str(task.tag_id)


                task_table1 = [task_id, task_title, task_description, task_category, task_tag]
                task_table.append(task_table1)
          return task_table
print(query_todo.fetch_all())
