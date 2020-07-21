def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for toppings in toppings:
        print("- " + toppings)

make_pizza(19, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')