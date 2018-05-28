# -*- coding: utf-8 -*-
from app import *

def create_tables():
    with database:
        database.create_tables([User, Relationship, Note])
        
if __name__ == '__name__':
    create_tables()