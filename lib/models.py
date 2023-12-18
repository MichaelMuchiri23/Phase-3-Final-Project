from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///todos.db')

Base = declarative_base()

#create category model
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

#printable object 
    def __repr__(self):
        return f'Category(id={self.id}, ' + \
            f'name={self.name})'
    
#create tag model
class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer(), primary_key=True)
    tag_name = Column(String())

    def __repr__(self):
        return f'Tag(id={self.id},' + \
            f'tag_name={self.tag_name})'
    
#create task model
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    description = Column(String())

    category_id = Column(Integer(), ForeignKey('categories.id'))
    tag_id = Column(Integer(), ForeignKey('tags.id'))

    def __repr__(self):
        return f'Task(id={self.id},' + \
            f'title={self.title},' + \
            f'description{self.description},' + \
            f'category_id={self.category_id},' + \
            f'tag_id={self.tag_id})'
