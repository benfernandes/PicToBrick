from abc import ABC, abstractmethod
from typing import Any, Iterable, Set, cast

# noinspection PyProtectedMember
from sqlalchemy.engine import RowProxy
from sqlalchemy.orm import Session

from pic_to_brick import brick
from pic_to_brick.database import model


class Query(ABC):
    @abstractmethod
    def query(self, session: Session) -> Iterable[RowProxy]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def build_result(result: Iterable[RowProxy]) -> Any:
        raise NotImplementedError


class AllColoursQuery(Query):
    def query(self, session: Session) -> Iterable[RowProxy]:
        return cast(
            Iterable[RowProxy],
            session.query(model.Colour).select_from(model.Colour).all()
        )

    @staticmethod
    def build_result(result: Iterable[RowProxy]) -> Set[brick.Colour]:
        return {brick.Colour(row.red, row.green, row.blue) for row in result}


class AllBricksQuery(Query):
    def query(self, session: Session) -> Iterable[RowProxy]:
        return cast(
            Iterable[RowProxy],
            session.query(model.Brick).select_from(model.Brick).all()
        )

    @staticmethod
    def build_result(result: Iterable[RowProxy]) -> Set[brick.Brick]:
        return {
            brick.Brick(
                brick.Colour(row.colour.red, row.colour.green, row.colour.blue),
                brick.Shape2D(row.width, row.height)
            ) for row in result
        }
