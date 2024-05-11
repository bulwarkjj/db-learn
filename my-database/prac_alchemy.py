import sqlalchemy as sa
import os
from lib.sql_engine import check_dir
import sys 

"""
Engine maintains a pool of connections, pools are like cache
"""
#engine = sa.create_engine(f"sqlite:////{os.path.join(os.getcwd(), 'test.db')}", echo=True)

# test engine connection
#engine.connect()

#meta = sa.MetaData()
#print(meta.reflect(engine))


"""
this create the table students, so I don't need to keep 
creating the table...or do I? I think this is where session maker
comes into play

-- Nope, I had to uncomment this to insert into students
"""
# students = sa.Table(
#     'students', meta,
#     sa.Column('id', sa.Integer, primary_key=True),
#     sa.Column('name', sa.String),
#     sa.Column('lastname', sa.String),
# )

# meta.create_all(engine)

"""
do perform anytype of expression, you need to connect first
this is what I'm doing with conn

so, use the engine to grab from the pool of connections
then connect() to perform expressions
"""

# with engine.connect() as conn:
    
"""
Sessions are used for Object Relationship Management(ORM)

uses connections and transactions for ORM

so if you are just doing straight SQL, where queries not bound to objects 
you are better off using connect()
"""

check_dir()