from conditions.base import Condition
from core.context import OrderContext


class UserTypeCondition(Condition):
    def __init__(self, user_type: str):
        self.user_type = user_type

    def is_satisfied(self, ctx: OrderContext) -> bool:
        return ctx.user_type == self.user_type