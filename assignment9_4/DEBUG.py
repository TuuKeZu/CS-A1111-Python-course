from restaurant_bill import RestaurantBill

t1 = RestaurantBill(1, "testi 1")
t2 = RestaurantBill(2, "testi 2")
t3 = RestaurantBill(3, "testi 3")

"""
t2.add_to_bill(12.20, False)
t1.add_to_bill(5.50, False)
t1.add_to_bill(5.50, False)

t2.add_to_bill(24.80, False)
t2.add_to_bill(13.40, False)
print("-----------")
print(t1)
print("-----------")
t1.add_to_bill(8.80, True)
print("-----------")
print(t1)
print("-----------")
t2.fix_price(2, False, 22.40)
t2.fix_price(1, False, 0.0)
t2.add_to_bill(11.50, True)
t2.add_to_bill(6.90, True)

print(t2.make_bill())
print(t1.make_bill())
print(t3.make_bill())
"""

t1.add_to_bill(13.40, False)
print(t1.fix_price(1, False, 7.90))
print(t1.make_bill())
