from typing import List
from core.context import OrderContext
from core.result import DiscountResult
from rules.base import DiscountRule
from conflicts.resolver import resolve_conflicts


class DiscountEngine:
    def __init__(self, rules: List[DiscountRule]):
        self.rules = rules

    def apply(self, ctx: OrderContext) -> List[DiscountResult]:
        applicable = [r for r in self.rules if r.applicable(ctx)]
        resolved = resolve_conflicts(applicable)
        return [r.apply(ctx) for r in resolved]