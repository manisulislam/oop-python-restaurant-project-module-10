from Menu import Burger, Drinks, Pizza, Menu
def main():
    menu= Menu()
    # pizza
    pizza_1= Pizza("sutki pizza",600, "large",["sutki", "onion", "oil"])
    menu.add_menu_item("pizza", pizza_1)
    pizza_2= Pizza("alor vorta pizza", 420, "big", ["potato", "oil"])
    menu.add_menu_item("pizza", pizza_2)
    pizza_3= Pizza("dal er pizza", 500, "small",["dal", "oil"])
    menu.add_menu_item("pizza", pizza_3)

    # burger
    burger_1= Burger("naga burger", 520,"chicken",["bread","chili"])
    menu.add_menu_item("burger", burger_1)
    burger_2 = Burger("beef burger", 6520, "beef", ["goro", "haddi"])
    menu.add_menu_item("burger", burger_2)
    
    # drinks
    coke= Drinks("coke", 50, True)
    menu.add_menu_item("drinks", coke)
    coffee = Drinks("mocha coffee", 120, False)
    menu.add_menu_item("drinks",coffee)

    # show menu
    menu.show_menu()
if __name__ == "__main__":
    main()