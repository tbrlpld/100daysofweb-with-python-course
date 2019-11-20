import sqlalchemy as sa
from sqlalchemy import orm

from data.models import __all
from db import db_folder


__engine = None
__factory = None


def init(db_name):
    """
    Initialize the engine and session factory.

    The initialized objects are stored in the module globals `__engine` and
    `__factory`.
    """
    global __engine, __factory

    # exit if the factory already exists
    if __factory is not None:
        return None

    db_connection = "sqlite:///" + db_folder.get_full_path(db_name)
    __engine = sa.create_engine(db_connection, echo=False)
    __factory = orm.sessionmaker(bind=__engine)


def create_tables():
    if __engine is None:
        print("Can not create tables, run init() first.")
        return None

    # The models need to be known. Since the import order is not clear,
    # import from this helper module.
    from data.models.base import Base

    Base.metadata.create_all(__engine)





