from conditions.base import Condition
from core.context import OrderContext


class MinTotalCondition(Condition):
    def __init__(self, min_total: float):
        self.min_total = min_total

    def is_satisfied(self, ctx: OrderContext) -> bool:
        return ctx.total >= self.min_total