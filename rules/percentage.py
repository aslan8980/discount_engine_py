from rules.base import DiscountRule
from core.context import OrderContext
from core.result import DiscountResult


class PercentageDiscountRule(DiscountRule):
    def __init__(self, rule_id, priority, stackable, conditions, percent):
        super().__init__(rule_id, priority, stackable, conditions)
        self.percent = percent

    def apply(self, ctx: OrderContext) -> DiscountResult:
        amount = ctx.total * self.percent / 100
        return DiscountResult(self.rule_id, amount, f"{self.percent}% discount")