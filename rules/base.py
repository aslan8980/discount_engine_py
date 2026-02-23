from abc import ABC, abstractmethod
from typing import List
from core.context import OrderContext
from core.result import DiscountResult
from conditions.base import Condition


class DiscountRule(ABC):
    def __init__(
        self,
        rule_id: str,
        priority: int,
        stackable: bool,
        conditions: List[Condition]
    ):
        self.rule_id = rule_id
        self.priority = priority
        self.stackable = stackable
        self.conditions = conditions

    def applicable(self, ctx: OrderContext) -> bool:
        return all(c.is_satisfied(ctx) for c in self.conditions)

    @abstractmethod
    def apply(self, ctx: OrderContext) -> DiscountResult:
        pass