#!/usr/bin/env python3
from models import Game
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    import ipdb; ipdb.set_trace()
