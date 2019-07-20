from abc import ABC, abstractmethod
from typing import Iterable, Any, Set

# noinspection PyProtectedMember
from sqlalchemy.engine import RowProxy

from pic_to_brick import brick
from pic_to_brick.database import model
from pic_to_brick.database.db_connection import DbSessionFactory


class Query(ABC):
    @abstractmethod
    def query(self, session) -> Iterable[RowProxy]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def build_result(result: Iterable[RowProxy]) -> Any:
        raise NotImplementedError


class AllColoursQuery(Query):
    # TODO - What type is session?
    def query(self, session) -> Iterable[RowProxy]:
        return session \
            .query(model.Colour) \
            .select_from(model.Colour) \
            .all()

    @staticmethod
    def build_result(result: Iterable[RowProxy]) -> Set[brick.Colour]:
        return {brick.Colour(row.red, row.green, row.blue) for row in result}


class AllBricksQuery(Query):
    # TODO - What type is session?
    def query(self, session) -> Iterable[RowProxy]:
        return session \
            .query(model.Brick) \
            .select_from(model.Brick) \
            .all()

    @staticmethod
    def build_result(result: Iterable[RowProxy]) -> Set[brick.Brick]:
        return {
            brick.Brick(
                brick.Colour(row.colour.red, row.colour.green, row.colour.blue),
                brick.Shape2D(row.width, row.height)
            ) for row in result
        }


class QueryRunner:
    def __init__(self, db_session_factory: DbSessionFactory):
        self.db_session_factory = db_session_factory

    def run_query(self, query: Query) -> Any:
        with self.db_session_factory.session_scope() as session:
            result = query.query(session)
            return query.build_result(result)
