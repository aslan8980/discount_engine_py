from dataclasses import dataclass
from typing import Optional, List


@dataclass
class OrderContext:
    total: float
    items: List[dict]
    user_type: str
    promo_code: Optional[str] = None