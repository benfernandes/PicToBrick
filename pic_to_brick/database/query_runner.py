from typing import Any

from pic_to_brick.database.db_connection import DbSessionFactory
from pic_to_brick.database.queries import Query


class QueryRunner:
    def __init__(self, db_session_factory: DbSessionFactory):
        self.db_session_factory = db_session_factory

    def run_query(self, query: Query) -> Any:
        with self.db_session_factory.session_scope() as session:
            result = query.query(session)
            return query.build_result(result)
