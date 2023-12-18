from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Tag

if __name__ == "__main__":
    engine = create_engine("sqlite:///todos.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete existing records before any insertion
    session.query(Category).delete()
    session.query(Tag).delete()
    
    #add data to category model
    categories=[
        Category(
        name = "outdoor",
    ),
    Category(
        name = "indoor",
    )
        
    ]
    
    #add data to tag model
    tags = [
        Tag(
        tag_name = "complete"
    ),
    Tag(
        tag_name = "incomplete"
    )

    ]
#commit and close session
    session.add_all(categories+ tags)
    session.commit()
    session.close()