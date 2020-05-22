from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class ModelCustomer(Base):
    """Customer model."""

    __tablename__ = "customers"

    id = Column("id", Integer, primary_key=True, doc="Id of the customer.")
    name = Column("name", String(32), doc="Name of the customer.")
    age = Column("age", Integer, doc="Customer's age")
    agent_id = Column(
        "agent_id",
        Integer,
        ForeignKey("agents.id"),
        doc="Id of the agent from which the customer buys from.",
    )
    created = Column("created", String(32), doc="Record created date.")
    edited = Column("edited", String(32), doc="Record last updated date.")
