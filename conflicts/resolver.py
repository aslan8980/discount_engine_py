from typing import List
from rules.base import DiscountRule


def resolve_conflicts(rules: List[DiscountRule]) -> List[DiscountRule]:
    rules = sorted(rules, key=lambda r: r.priority, reverse=True)
    result = []
    for rule in rules:
        if not result:
            result.append(rule)
            continue
        if rule.stackable:
            result.append(rule)
    return result