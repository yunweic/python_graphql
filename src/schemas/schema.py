from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
from schemas import schema_agent
from schemas import schema_customer


class Query(graphene.ObjectType):
    """Nodes which can be queried by this API."""

    node = graphene.relay.Node.Field()

    # Agent
    agent = graphene.relay.Node.Field(schema_agent.Agent)
    agentList = SQLAlchemyConnectionField(schema_agent.Agent)

    # Customer
    customer = graphene.relay.Node.Field(schema_customer.Customer)
    customerList = SQLAlchemyConnectionField(schema_customer.Customer)


class Mutation(graphene.ObjectType):
    """Mutations which can be performed by this API."""

    # Agennt mutation
    createAgent = schema_agent.CreateAgent.Field()
    updateAgent = schema_agent.UpdateAgent.Field()

    # Customer mutatio
    createCustomer = schema_customer.CreateCustomer.Field()
    updateCustomer = schema_customer.UpdaterCustomer.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
