from abc import ABC, abstractmethod
from core.context import OrderContext


class Condition(ABC):
    @abstractmethod
    def is_satisfied(self, ctx: OrderContext) -> bool:
        pass