from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_customer import ModelCustomer
import graphene
import utils
from flask_jwt_extended import jwt_required

# Create a generic class to mutualize description of customer attributes for both queries and mutations
class CustomerAttribute:
    name = graphene.String(description="Name of the customer.")
    age = graphene.Int(description="Agent's age")

    agent_id = graphene.ID(
        description="Global Id of the planet from which the customer comes from."
    )


class Customer(SQLAlchemyObjectType):
    """Customer node."""

    class Meta:
        model = ModelCustomer
        interfaces = (graphene.relay.Node,)


class CreateCustomerInput(graphene.InputObjectType, CustomerAttribute):
    """Arguments to create a customer."""

    pass


class CreateCustomer(graphene.Mutation):
    """Mutation to create a customer."""

    customer = graphene.Field(
        lambda: Customer, description="Customer created by this mutation."
    )

    class Arguments:
        input = CreateCustomerInput(required=True)

    @jwt_required
    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data["created"] = datetime.utcnow()
        data["edited"] = datetime.utcnow()

        customer = ModelCustomer(**data)
        db_session.add(customer)
        db_session.commit()

        return CreateCustomer(customer=customer)


class UpdateCustomerInput(graphene.InputObjectType, CustomerAttribute):
    """Arguments to update a customer."""

    id = graphene.ID(required=True, description="Global Id of the customer.")


class UpdaterCustomer(graphene.Mutation):
    """Update a customer."""

    customer = graphene.Field(
        lambda: Customer, description="Customer updated by this mutation."
    )

    class Arguments:
        input = UpdateCustomerInput(required=True)

    @jwt_required
    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data["edited"] = datetime.utcnow()

        customer = db_session.query(ModelCustomer).filter_by(id=data["id"])
        customer.update(data)
        db_session.commit()
        customer = db_session.query(ModelCustomer).filter_by(id=data["id"]).first()

        return UpdaterCustomer(customer=customer)
