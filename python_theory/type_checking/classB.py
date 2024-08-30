from typing import TYPE_CHECKING, Optional

# to pass type checking
if TYPE_CHECKING:
    from classA import A


class B:
    def __init__(self, A_obj: Optional['A'] = None) -> None:
        self.A_obj = A_obj