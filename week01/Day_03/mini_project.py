"""
🛠️ Mini Project · Shopping Cart (LLD) (1 hr) · week01/day04/shopping_cart.py

This is a classic low-level design interview question. Money is stored in integer cents (Day 1 lesson!).

Classes to build:

Class	Responsibilities
Product(sku, name, price_cents)	ValueError if price ≤ 0. __eq__/__hash__ by sku. __repr__
Discount (ABC)	abstract amount_off(subtotal_cents) -> int
PercentOff(percent)	ValueError unless 0 < percent ≤ 100. Discount = subtotal * percent // 100
FlatOff(cents)	discount = cents, but never more than the subtotal (total can't go negative)
Cart	stores lines in a dict keyed by sku (why? Big-O!). add(product, qty=1) merges into an existing line;
        remove(sku) raises KeyError if absent; __len__ = total item count; subtotal_cents();
        apply(discount) (one discount at a time, replaces previous); total_cents(); __repr__

Also write a helper format_money(cents: int) -> str (19493 → "$194.93", 5 → "$0.05", 123456789 → "$1,234,567.89").
Don't use float. Hint: // and % by 100.

Driver code (paste at the bottom):

python
keyboard = Product("KB-1", "Mechanical Keyboard", 8999)
mouse = Product("MS-1", "Wireless Mouse", 2499)
cable = Product("CB-1", "USB-C Cable", 999)

cart = Cart()
cart.add(keyboard)
cart.add(mouse, 2)
cart.add(cable, 3)
cart.add(mouse)                         # merges → mouse qty 3
print(len(cart))
print(format_money(cart.subtotal_cents()))
cart.apply(PercentOff(10))
print(format_money(cart.total_cents()))
cart.remove("CB-1")
print(cart)
cart.apply(FlatOff(50_000))
print(format_money(cart.total_cents()))
print(mouse == Product("MS-1", "Mouse v2", 1999), len({mouse, Product("MS-1", "x", 1)}))

for bad in (lambda: Product("X", "x", 0), lambda: cart.add(mouse, 0), lambda: cart.remove("NOPE")):
    try:
        bad()
    except (ValueError, KeyError) as e:
        print(type(e).__name__, e)

Expected output:

7
$194.93
$175.44
Cart(lines=2, items=4, total=$148.47)
$0.00
True 1
ValueError price must be positive
ValueError qty must be positive
KeyError 'NOPE'

Stretch: add MinSpend(threshold_cents, inner_discount), which applies inner_discount only if the subtotal ≥ threshold.
This is composition (a discount that has a discount). Explain in a comment why that beats making it a subclass.
"""