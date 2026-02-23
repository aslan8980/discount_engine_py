from rules.base import DiscountRule
from core.context import OrderContext
from core.result import DiscountResult


class FixedDiscountRule(DiscountRule):
    def __init__(self, rule_id, priority, stackable, conditions, amount):
        super().__init__(rule_id, priority, stackable, conditions)
        self.amount = amount

    def apply(self, ctx: OrderContext) -> DiscountResult:
        return DiscountResult(self.rule_id, self.amount, "Fixed discount")