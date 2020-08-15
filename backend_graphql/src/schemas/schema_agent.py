from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_agent import ModelAgent
import graphene
import utils


# Create a generic class to mutualize description of agent attributes for both queries and mutations
class AgentAttribute:
    name = graphene.String(description="Name of the agent.")
    age = graphene.Int(description="Agent's age")


class Agent(SQLAlchemyObjectType):
    """Agent node."""

    class Meta:
        model = ModelAgent
        interfaces = (graphene.relay.Node,)


class CreateAgentInput(graphene.InputObjectType, AgentAttribute):
    """Arguments to create a agent."""

    pass


class CreateAgent(graphene.Mutation):
    """Create a agent."""

    agent = graphene.Field(lambda: Agent, description="Agent created by this mutation.")

    class Arguments:
        input = CreateAgentInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data["created"] = datetime.utcnow()
        data["edited"] = datetime.utcnow()

        agent = ModelAgent(**data)
        db_session.add(agent)
        db_session.commit()

        return CreateAgent(agent=agent)


class UpdateAgentInput(graphene.InputObjectType, AgentAttribute):
    """Arguments to update a agent."""

    id = graphene.ID(required=True, description="Global Id of the agent.")


class UpdateAgent(graphene.Mutation):
    """Update a agent."""

    agent = graphene.Field(lambda: Agent, description="Agent updated by this mutation.")

    class Arguments:
        input = UpdateAgentInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data["edited"] = datetime.utcnow()

        agent = db_session.query(ModelAgent).filter_by(id=data["id"])
        agent.update(data)
        db_session.commit()
        agent = db_session.query(ModelAgent).filter_by(id=data["id"]).first()

        return UpdateAgent(agent=agent)
