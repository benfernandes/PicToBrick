from typing import List, Iterable

# noinspection PyProtectedMember
from sqlalchemy.engine import RowProxy

from pic_to_brick import brick
from pic_to_brick.database import model
from pic_to_brick.database.db_connection import DbSessionFactory


class QueryRunner:
    def __init__(self, db_session_factory: DbSessionFactory):
        self.db_session_factory = db_session_factory

    def get_all_colours(self) -> List[brick.Colour]:
        with self.db_session_factory.session_scope() as session:
            result = session.query(model.Colour).select_from(model.Colour).all()

            return self._build_result(result)

    @staticmethod
    def _build_result(result: Iterable[RowProxy]) -> List[brick.Colour]:
        return [brick.Colour(row.red, row.green, row.blue) for row in result]

# TODO - This should be a get_all_bricks method
