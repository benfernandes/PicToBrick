from typing import Any


class ArgumentError(Exception):
    def __init__(self, argument: str, *args: Any) -> None:
        super().__init__(f'Error: No "{argument}" field provided. Please specify "{argument}" as a param.', *args)
