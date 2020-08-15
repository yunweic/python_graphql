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
