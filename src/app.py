from database.base import db_session
from flask import Flask
from flask_graphql import GraphQLView
from schemas.schema import schema


def create_app():
    app = Flask(__name__)
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, threaded=True)  # debug=True


# from flask import Flask
# from flask_graphql import GraphQLView
# # from flask_restful import Api

# from models.models import db_session
# from schema import schema, Agent

# import config
# # from models import agents

# from db import db


# def create_app():

#     app = Flask(__name__)
#     # app.debug = True

#     # @app.teardown_appcontext
#     # def shutdown_session(exception=None):
#     #     db_session.remove()

#     app.add_url_rule(
#         '/graphql',
#         view_func=GraphQLView.as_view(
#             'graphql',
#             schema=schema,
#             graphiql=True # for having the GraphiQL interface
#         )
#     )

#     # ##################
#     # Database setup
#     app.config["SQLALCHEMY_DATABASE_URI"] = (
#         "mysql+mysqlconnector://"
#         + config.MYSQL_USER
#         + ":"
#         + config.MYSQL_PASSWORD
#         + "@"
#         + config.MYSQL_IP
#         + ":"
#         + config.MYSQL_PORT
#         + "/"
#         + config.MYSQL_DATABASE
#     )
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#     return app

# if __name__ == "__main__":

#     app = create_app()
#     db.init_app(app)

#     app.run(debug=True)
