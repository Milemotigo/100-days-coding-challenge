from sqlalchemy.orm import declarative_base, sessionmaker
'''from declarative_base is where we create our base class from which we inherit to 
create our schema table'''
'''we store objects in a database'''

from sqlalchemy import Column,  String, Integer, DateTime, create_engine
from datetime import datetime
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
connection_string="sqlite:///"+os.path.join(BASE_DIR,'site.db')

Base=declarative_base()

engine = create_engine(connection_string,echo=True)


Session=sessionmaker()
"""
class User
    id int
    username str
    email str
    date_created datetime
"""
class User(Base):
    __tablename__='users'
    id = Column(Integer(), primary_key=True)
    username=Column(String(25), nullable=False, unique=True)
    email=Column(String(80), nullable=False, unique=True)
    date_create=Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<User username={self.username}, User email={self.email}>"
        #return(new_user)
new_user = User(id=1,username='favor', email='fav@gmail.company')
print(new_user)