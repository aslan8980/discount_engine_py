from core.context import OrderContext
from core.engine import DiscountEngine
from loaders.rule_loader import load_rules


ctx = OrderContext(
    total=120,
    items=[],
    user_type="new",
    promo_code=None
)

rules = load_rules("examples/rules.json")
engine = DiscountEngine(rules)

results = engine.apply(ctx)

for r in results:
    print(r)