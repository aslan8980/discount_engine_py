from conditions.base import Condition
from core.context import OrderContext


class PromoCodeCondition(Condition):
    def __init__(self, code: str):
        self.code = code

    def is_satisfied(self, ctx: OrderContext) -> bool:
        return ctx.promo_code == self.code