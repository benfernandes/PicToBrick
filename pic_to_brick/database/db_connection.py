from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import database_exists


class DbSessionFactory:
    def __init__(self, db_connection_str: str) -> None:
        if not database_exists(db_connection_str):
            raise Exception(f'Database with connection {db_connection_str} not found.')
        self.engine = create_engine(db_connection_str)
        session_maker = sessionmaker(bind=self.engine)
        self._session = session_maker()

    @contextmanager
    def session_scope(self) -> Session:
        try:
            yield self._session
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
        finally:
            self._session.close()
