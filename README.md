# Discount Engine

A rule-based discount calculation engine written in pure Python.

This project demonstrates how to design flexible and extensible backend business logic without relying on if-else chains, frameworks, or external dependencies.

---

## 🚀 Features

- Rule-based discount system
- Extensible architecture (add new rules without changing existing code)
- Condition-driven logic (clean separation of concerns)
- Conflict resolution (priority + stackability)
- JSON-based configuration
- Pure Python (standard library only)

---

## 📦 Project Structure


discount_engine/
├── core/ # Engine, context, result models
├── rules/ # Discount rule implementations
├── conditions/ # Rule conditions
├── conflicts/ # Conflict resolution logic
├── loaders/ # JSON rule loader
├── examples/ # Demo usage
└── tests/ # (optional)


---

## ⚙️ How It Works

1. **OrderContext** holds all input data (total, user, promo code, etc.)
2. **Conditions** determine if a rule is applicable
3. **Rules** define how discounts are calculated
4. **Engine** applies rules and resolves conflicts
5. **Loader** builds rules dynamically from JSON

---

## ▶️ Run Example

```bash

PYTHONPATH=. python3 examples/run_example.py

Example output:

DiscountResult(rule_id='WELCOME10', amount=12.0, description='10% discount')
📄 Example Rule (JSON)
{
  "id": "WELCOME10",
  "type": "percentage",
  "value": 10,
  "priority": 100,
  "stackable": false,
  "conditions": [
    { "type": "user_type", "value": "new" },
    { "type": "min_total", "value": 50 }
  ]
}
🧠 What This Project Demonstrates
Clean backend architecture
Separation of business logic from configuration
Use of polymorphism instead of condition-heavy code
Extensible system design (open for extension, closed for modification)
Real-world use case (e-commerce / fintech discount systems)
📌 Notes
No frameworks used
No database required
Designed for clarity and architecture demonstration
📎 Future Improvements (optional)
Unit tests
Advanced conflict strategies (best discount selection)
Explainability (why rules were applied or rejected)
