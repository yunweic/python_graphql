from database import base
from database.model_agent import ModelAgent

if __name__ == '__main__':
    # log.info('Create database {}'.format(base.db_name))
    # print(base)
    # print(type(base))
    base.Base.metadata.create_all(base.engine, checkfirst=True)

    # log.info('Insert Planet data in database')
    # with open('database/data/planet.json', 'r') as file:
    #     data = literal_eval(file.read())
    #     for record in data:
    #         planet = ModelPlanet(**record)
    #         base.db_session.add(planet)
    #         base.db_session.commit()

    # log.info('Insert People data in database')
    # with open('database/data/people.json', 'r') as file:
    #     data = literal_eval(file.read())
    #     for record in data:
    #         planet = ModelPeople(**record)
    #         base.db_session.add(planet)
    #         base.db_session.commit()
