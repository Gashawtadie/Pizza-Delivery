from add_extra import extra
from lists_class import sizes_prices
from lists_class import total
from deliver_pi import deliver


def size_pizza():
    size = input("Select size please: ")
    extra()
    if size in sizes_prices and deliver() == "y":

        price1 = sizes_prices[size] + 20 + 2
        total.append(price1)
    else:
        price2 = sizes_prices[size] + 60
        total.append(price2)
