from database import base
from database.model_agent import ModelAgent

if __name__ == "__main__":

    base.Base.metadata.create_all(base.engine, checkfirst=True)
