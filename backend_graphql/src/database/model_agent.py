from database.base import Base
from database.model_customer import ModelCustomer
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ModelAgent(Base):
    """Agent model."""

    __tablename__ = "agents"

    id = Column("id", Integer, primary_key=True, doc="Id of the person.")
    name = Column("name", String(32), doc="Name of the agent.")
    age = Column("age", Integer, doc="Agent's age")
    created = Column("created", String(32), doc="Record created date.")
    edited = Column("edited", String(32), doc="Record last updated date.")

    customerList = relationship(ModelCustomer, backref="customers")
