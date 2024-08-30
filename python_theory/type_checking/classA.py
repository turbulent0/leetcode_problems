from typing import TYPE_CHECKING, Optional

# to pass type checking
if TYPE_CHECKING:
    from classB import B


class A:
    def __init__(self, B_obj: Optional['B'] = None) -> None:
        self.B_obj = B_obj

