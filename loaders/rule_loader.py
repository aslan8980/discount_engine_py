import json
from conditions.min_total import MinTotalCondition
from conditions.user_type import UserTypeCondition
from conditions.promo_code import PromoCodeCondition
from rules.percentage import PercentageDiscountRule
from rules.fixed import FixedDiscountRule


CONDITION_REGISTRY = {
    "min_total": MinTotalCondition,
    "user_type": UserTypeCondition,
    "promo_code": PromoCodeCondition,
}

RULE_REGISTRY = {
    "percentage": PercentageDiscountRule,
    "fixed": FixedDiscountRule,
}


def load_rules(path: str):
    with open(path) as f:
        data = json.load(f)

    rules = []
    for r in data:
        conditions = [
            CONDITION_REGISTRY[c["type"]](c["value"])
            for c in r.get("conditions", [])
        ]
        rule_cls = RULE_REGISTRY[r["type"]]
        rule = rule_cls(
            r["id"],
            r["priority"],
            r["stackable"],
            conditions,
            r["value"],
        )
        rules.append(rule)
    return rules