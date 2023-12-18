from sqlalchemy import insert
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Tag, Task

engine = create_engine('sqlite:///todos.db')
Session = sessionmaker(bind=engine)
session = Session()


class query_todo():

    #create task
    def create(todo):
            task = Task(title=todo[0], description=todo[1], category_id=todo[2], tag_id=todo[3])
            session.add(task)
            session.commit()

    #fetch all tasks from task table
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
    
    #update task in task table
    def update_task(task_id, new_title=None, new_description=None, new_category_id=None, new_tag_id=None):
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description
            if new_category_id:
                task.category_id = new_category_id
            if new_tag_id:
                task.tag_id = new_tag_id
            session.commit()
            return True
        else:
            return "Task with ID {} not found".format(task_id)  # Return error message if task not found
        
    #delete a task from the database
    def delete_task(task_id):
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            session.delete(task)
            session.commit()
            return True
        else:
            return "Task with ID {} not found".format(task_id)  # Return error message if task not found  
        
    #filter tasks displayed by tag id
    def fetch_by_tag(tag_id):
        tasks = session.query(Task).filter_by(tag_id=tag_id).all()
        task_table = []

        for task in tasks:
            task_id = str(task.id)
            task_title = task.title
            task_description = task.description
            task_category = str(task.category_id)
            task_tag = str(task.tag_id)

            task_table1 = [task_id, task_title, task_description, task_category, task_tag]
            task_table.append(task_table1)

        return task_table
      




    