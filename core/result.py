from dataclasses import dataclass


@dataclass
class DiscountResult:
    rule_id: str
    amount: float
    description: str