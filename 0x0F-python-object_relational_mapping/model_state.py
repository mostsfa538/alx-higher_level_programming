#!/usr/bin/python3
"""Here goes everything"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """class state"""
    __tablename__ = "state"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
